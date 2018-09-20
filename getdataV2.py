from pysnmp.entity.rfc3413.oneliner import cmdgen


# cmdGen = cmdgen.CommandGenerator()


class Get_PortInfo():
    def __init__(self, Community, IPAdd, StartInterfaceID, EndInterfaceID):
        cmdGen = cmdgen.CommandGenerator()
        errorIndication, errorStatus, errorIndex, varBinds = cmdGen.getCmd(
            cmdgen.CommunityData(Community),
            cmdgen.UdpTransportTarget((IPAdd, 161)),
            # cmdgen.ContextData(),
            StartInterfaceID = int(StartInterfaceID)
            EndInterfaceID = int(EndInterfaceID)
            while StartInterfaceID == EndInterfaceID:

                '1.3.6.1.2.1.2.2.1.2.'+InterfaceID,
                lookupNames=True, lookupValues=True
            )

        name = str(varBinds[0])
        self.name = (name[-19:])
        print(self.name)
