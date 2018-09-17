import pexpect
import getpass

HOST = "192.168.1.5"
#user = raw_input("Enter your remote account: ")
password = getpass.getpass()

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
child.sendline('reload')
child.sendline('\n')
