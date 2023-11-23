from pydantic import BaseModel

class SystemInfoLog(BaseModel):
    System: str
    NodeName: str
    Release: str
    Version: str
    Machine: str
    Processor: str
    Hostname: str
    IPAddress: str
    User: str
    FirewallStatus: str
    AntivirusStatus: str
    