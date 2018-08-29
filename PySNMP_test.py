from pysnmp.hlapi import *

errorIndication, errorStatus, errorIndex, varBinds = next(
    getCmd(SnmpEngine(),
           CommunityData('H5'),
           UdpTransportTarget(('192.168.1.5', 161)),
           ContextData(),
           ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)))
)

if errorIndication:



    print(errorIndication)

elif errorStatus:
    print('%s at %s' % (errorStatus.prettyPrint(),
                        errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
else:
    for varBind in varBinds:
        print(' = '.join([x.prettyPrint() for x in varBind]))



from pysnmp.hlapi.asyncore import UdpTransportTarget
UdpTransportTarget(('google.com', 161)),
UdpTransportTarget(('google.com', 161), timeout=1, retries=5, tagList='')
