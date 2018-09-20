from pysnmp.entity.rfc3413.oneliner import cmdgen


# cmdGen = cmdgen.CommandGenerator()


class Get_PortInfo_Range():

    def __init__(self, Community, IPAdd, StartInterfaceID = 0, EndInterfaceID = 0):
        cmdGen = cmdgen.CommandGenerator()
        self.name= []
        while StartInterfaceID <= EndInterfaceID:
            InterfaceID = str(StartInterfaceID)
            errorIndication, errorStatus, errorIndex, varBinds = cmdGen.getCmd(
                cmdgen.CommunityData(Community),
                cmdgen.UdpTransportTarget((IPAdd, 161)),

                '1.3.6.1.2.1.2.2.1.2.'+InterfaceID,
                #'1.3.6.1.2.1.2.2.1.9.'+InterfaceID,
                lookupNames=True, lookupValues=True
                )
            StartInterfaceID = StartInterfaceID+1

            name = str(varBinds[0])
            self.name.append (name[-19:])
            print(self.name)
