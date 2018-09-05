from pysnmp.hlapi import *

errorIndication, errorStatus, errorIndex, varBinds = next(
    getCmd(SnmpEngine(),
           CommunityData('H5'),
           UdpTransportTarget(('192.168.1.5', 161)),
           ContextData(),
           #ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)),
           ObjectType(ObjectIdentity('1.3.6.1.2.1.1.1')))
)
'''varBinds = [
    ('1.3.6.1.2.1.1.3.0', 12345),
    ('1.3.6.1.6.3.1.1.4.1.0', '1.3.6.1.6.3.1.1.5.2'),
    ('1.3.6.1.6.3.18.1.3.0', '0.0.0.0'),
    ('1.3.6.1.6.3.18.1.4.0', ''),
    ('1.3.6.1.6.3.1.1.4.3.0', '1.3.6.1.4.1.20408.4.1.1.2'),
    ('1.3.6.1.2.1.1.1.0', 'my system')
]

varBinds = [rfc1902.ObjectType(rfc1902.ObjectIdentity(x[0]), x[1]).resolveWithMib(mibViewController) for x in varBinds]

for varBind in varBinds:
    print(varBind.prettyPrint())
'''
if errorIndication:



    print(errorIndication)

elif errorStatus:
    print('%s at %s' % (errorStatus.prettyPrint(),
                        errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
else:
    for varBind in varBinds:
        print(' = '.join([x.prettyPrint() for x in varBind]))
