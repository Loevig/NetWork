from pysnmp.hlapi import *

class SNMP_NAME_CLASS(object):
    """docstring for SNMP_NAME_CLASS."""
    def __init__(self, arg):
        super(SNMP_NAME_CLASS, self).__init__()
        self.arg = arg
        
errorIndication, errorStatus, errorIndex, varBinds = next(
    getCmd(SnmpEngine(),
           CommunityData('H5'),
           UdpTransportTarget(('192.168.1.5', 161)),
           ContextData(),
           ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)),
           ObjectType(ObjectIdentity('IF-MIB', 'ifNumber', 0)),
           ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.15.10101')),
           ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.8.5')),
           ObjectType(ObjectIdentity('1.3.6.1.2.1.1.1.0')))
)


if errorIndication:



    print(errorIndication)

elif errorStatus:
    print('%s at %s' % (errorStatus.prettyPrint(),
                        errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
else:
    for varBind in varBinds:
        print(' = '.join([x.prettyPrint() for x in varBind]))
