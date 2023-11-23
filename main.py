from fastapi import FastAPI
from routes.route import router, overallStatus, agentIDs    
import time, threading


app = FastAPI()
app.include_router(router)

def healthcheckmon():
    '''
        Function to poll status and revert to DOWN if no communication after 60 seconds 
    '''
    while True:
        for i in agentIDs:
            if overallStatus[str(i)]["LastPing"] < time.time() - 60:
                overallStatus[str(i)]["Status"] = "DOWN"
        time.sleep(20)

x = threading.Thread(target=healthcheckmon, args=())
x.daemon = True
x.start()