from pysnmp.hlapi import *

mib = {ObjectIdentifier('1.3.6.1.2.1.2.2.1.1.1'): 1,
        ObjectIdentifier('1.3.6.1.2.1.2.2.1.7.1'): 'testing',
        ObjectIdentifier('1.3.6.1.2.1.2.2.1.8.1'): 'up'}

g = sendNotification(SnmpEngine(),
                      CommunityData('H5'),
                      UdpTransportTarget(('192.168.1.5', 161)),
                      ContextData(),
                      'inform',
                      NotificationType(ObjectIdentity('IF-MIB', 'linkUp'), instanceIndex=(1,), objects=mib)
)
