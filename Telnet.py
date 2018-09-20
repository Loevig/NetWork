import pexpect

class telnet_super():
    """docstring for telnet_super."""
    def __init__(self, IPadd, hostname, password):

        self.HOST = IPadd
        #user = raw_input("Enter your remote account: ")
        self.password = password
        self.child = pexpect.spawn('telnet '+self.HOST)
        print("login")
        self.child.expect('Password: ')
        self.child.sendline(self.password)
        # If the hostname of the router is set to "deep"
        # then the prompt now would be "deep>"
        routerHostname = hostname  # example - can be different
        self.child.expect(routerHostname+'>')
        print("super")


    def reload(self):
        self.child = pexpect.spawn('telnet '+self.HOST)
        self.child.sendline(self.password)
        self.child.sendline('enable')
        self.child.sendline(self.password)
        self.child.sendline('reload')
        #self.child.sendline('no')
        self.child.sendline('\n')

    def config_interface_range_Vlan(self, interfaceRange, vlan):
        self.child = pexpect.spawn('telnet '+self.HOST)
        self.child.sendline(self.password)
        self.child.sendline('enable')
        self.child.sendline(self.password)
        self.child.sendline ('conf t')
        for l in interfaceRange:
            self.child.sendline('interface '+ l)
            self.child.sendline('sw mode acc')
            self.child.sendline('sw acc vl '+vlan)

'''class Telnet_Reload(telnet_super):
    def __init__(self):
        super(self).__init__()
        super.child.sendline('enable')
        super.child.sendline(super.password)
        super.child.sendline ('reload')
        super.child.sendline('\n')
'''
