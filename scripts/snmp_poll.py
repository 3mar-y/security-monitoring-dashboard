#!/usr/bin/env python3

from pysnmp.hlapi import *

def poll_snmp(host, community, oid):
    iterator = getCmd(
        SnmpEngine(),
        CommunityData(community),
        UdpTransportTarget((host, 161)),
        ContextData(),
        ObjectType(ObjectIdentity(oid))
    )

    for errorIndication, errorStatus, errorIndex, varBinds in iterator:
        if errorIndication:
            print(f"Error: {errorIndication}")
        elif errorStatus:
            print(f"Error: {errorStatus.prettyPrint()}")
        else:
            for varBind in varBinds:
                print(f"{varBind}")

if __name__ == "__main__":
    # Example: poll system description from a device
    poll_snmp("192.168.1.1", "public", "1.3.6.1.2.1.1.1.0")
