from pysnmp.entity.rfc3413.oneliner import cmdgen


#cmdGen = cmdgen.CommandGenerator()


class Get_PortInfo():
    cmdGen = cmdgen.CommandGenerator()
    errorIndication, errorStatus, errorIndex, varBinds = cmdGen.getCmd(
        cmdgen.CommunityData('H5'),
        cmdgen.UdpTransportTarget(('192.168.1.5', 161)),
        #cmdgen.ContextData(),
        '1.3.6.1.2.1.2.2.1.2.10101',
        lookupNames=True, lookupValues=True
        )


    name = str(varBinds[0])
    print(name[-18:])
