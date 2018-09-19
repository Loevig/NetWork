from pysnmp.hlapi import *

class SNMP_PORTINFO_ClASS():
    """docstring for SNMP_CLASS."""
    def __init__(self, MIBOID_ARG):
        #super(SNMP_CLASS, self).__init__()
        errorIndication, errorStatus, errorIndex, varBinds = next(
            getCmd(SnmpEngine(),
                   CommunityData('H5'),
                   UdpTransportTarget(('192.168.1.5', 161)),
                   ContextData(),
                   ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.'+ MIBOID_ARG))
))

        if errorIndication:



            print(errorIndication)

        elif errorStatus:
            print('%s at %s' % (errorStatus.prettyPrint(),
                                errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
        else:
            for varBind in varBinds:
                print(' = '.join([x.prettyPrint() for x in varBind]))

#G1NAME = SNMP_PORTINFO_ClASS('2.10101')
#G1STAUS = SNMP_PORTINFO_ClASS('6.10101')
