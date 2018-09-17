from ciscoconfparse import CiscoConfParse

BASELINE = """!
... interface Vlan 1
...  ip address 10.0.0.1 255.255.255.0
... !""".splitlines()

parse = CiscoConfParse(BASELINE)
