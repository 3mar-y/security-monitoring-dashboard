#!/usr/bin/env python3

from pysnmp.hlapi import *

def poll_snmp(host, community, oids):
    for oid in oids:
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
                    print(f"{oid} -> {varBind}")

if __name__ == "__main__":
    # Example: poll multiple system OIDs
    target_host = "192.168.1.1"   # Replace with your device IP
    community = "public"          # Replace with your SNMP community string
    oids = [
        "1.3.6.1.2.1.1.1.0",  # System description
        "1.3.6.1.2.1.1.5.0"   # System name
    ]
    poll_snmp(target_host, community, oids)
