import getdataV2
import Telnet
IPadd ='192.168.1.5'
G1NAME = getdataV2.Get_PortInfo_Range_IF0('H5', IPadd, 10101, 10124)

test = Telnet.telnet_super(IPadd, 'H5-prog', 'cisco')
#test.reload()
test.config_interface_range_Vlan(G1NAME.name, '666')

'''HOST = "192.168.1.5"
#user = raw_input("Enter your remote account: ")
password = 'cisco'

child = pexpect.spawn('telnet '+HOST)
child.expect('Password: ')
child.sendline(password)
# If the hostname of the router is set to "deep"
# then the prompt now would be "deep>"
routerHostname = "H5-prog"  # example - can be different
child.expect(routerHostname+'>')
child.sendline('enable')
child.sendline(password)
child.sendline ('conf t')
for l in G1NAME.name:
    child.sendline('interface '+ l)
    child.sendline('sw mode acc')
    child.sendline('sw acc vl 666')
'''
