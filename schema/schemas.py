def individual_serial(SystemInfoLog) -> dict:
    return {
        "id": str(SystemInfoLog["_id"]),
        "NodeName": SystemInfoLog["Node Name"],
        "System": SystemInfoLog["System"],
        "Release": SystemInfoLog["Release"],
        "Version": SystemInfoLog["Version"],
        "Machine": SystemInfoLog["Machine"],
        "Processor": SystemInfoLog["Processor"],
        "Hostname": SystemInfoLog["Hostname"],
        "IPAddress": SystemInfoLog["IP Address"],
        "User": SystemInfoLog["User"],
        "FirewallStatus": SystemInfoLog["Firewall Status"],
        "AntivirusStatus": SystemInfoLog["Antivirus Status"]
    }
    
def list_serial(SystemInfoLogs) -> list:
        return [individual_serial(SystemInfoLog) for SystemInfoLog in SystemInfoLogs]