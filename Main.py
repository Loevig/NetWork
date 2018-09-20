import getdataV2
import pexpect
import getpass
G1NAME = getdataV2.Get_PortInfo_Range('H5', '192.168.1.5', 10101, 10124)




HOST = "192.168.1.5"
#user = raw_input("Enter your remote account: ")
password = 'cisco'

child = pexpect.spawn('telnet '+HOST)
#child.expect('Username: ')
#child.sendline(user)
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
    child.sendline('no sh')
