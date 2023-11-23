from fastapi import APIRouter, HTTPException, Query, Request, Body
from models.logs import SystemInfoLog
from config.database import client, db
from schema.schemas import list_serial
from bson import ObjectId
import time

router = APIRouter()
agentIDs = [1,2,3,4,5]
logTypes = ["SystemInfo","EventViewerApplication","EventViewerSystem", "EventViewerSecurity"]
collection_name = db["SystemInfoLogs"]
overallStatus = {}
for agent in agentIDs:
    overallStatus[str(agent)] = {"Status":"Down", "LastPing": time.time()-80}

# TO-DO
# Add method to update/pull agent settings w/validation
# Add method to create/push agent settings w/validation
# Add method to get static information for website population based on page (query Hostname, IPs etc.)

@router.get("/healthcheck/fetch/")
async def healthCheckFetch():
    '''
        This endpoint is for retrieving the healthcheck status
    '''
    return overallStatus

@router.get("/healthcheck/")
async def healthCheck(agentid: str):
    '''
        This endpoint is for doing frequent health checks, will be used to display live data on system status throughout the webpage.
        Agent pings endpoint, sets status to UP.
        After x time, with no ping, reset status to DOWN
    '''
    if int(agentid) in agentIDs:
        overallStatus[str(agentid)] = {"Status":"UP", "LastPing": time.time()}
        return "Good to see you!"
    else:
        return "Invalid Agent"


@router.get("/query/")
async def get_data(key: str = Query(None, title="Key", description="Search key", min_length=1),
                   value: str = Query(None, title="Value", description="Search value", min_length=1),
                   collec: str = Query(None, title="Collec", description="Search collection", min_length=1)):
    '''
        This endpoint is for doing basic queries based on MongoDB Collection, Key, and Value
    '''
    try:
        query = {key: value}
        # Query documents in the collection based on the provided key-value pair
        if collec in logTypes:
            collection_name = db[collec]
        r = collection_name.find(query)
        k = []
        for i in r:
            i["_id"] = str(i["_id"])
            k.append(i) 
        return k
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.post("/logingestor/")
async def save_log(
        payload: dict = Body(None)
        ):
    '''
        This endpoint is for ingesting logs, accepts modified json dict with two keys + body:
        XUFIAGENTID
        XUFILOGTYPE

        These allow for authorization / organization into DB
    '''
    try:

        strtmp = logRequestSorter(payload)
        return strtmp
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
def logRequestSorter(logToIngest):
    global collection_name
    print(logToIngest)
    agentid = logToIngest["XUFIAGENTID"]
    logtype = logToIngest["XUFILOGTYPE"]
    
    agentcheck = False
    logcheck = False
    if agentid in agentIDs:
        agentcheck = True
    if logtype in logTypes:
        logcheck = True
    if agentcheck and logcheck:
        collection_name = db[logtype]
        collection_name.insert_one(logToIngest)
        return "Ingestion Success"
    elif not agentcheck:
        return "Unknown Agent"
    elif not logcheck:
        return "Unknown Log Type"
    else:
        return "Unknown Request"