#!/usr/bin/python

import dns.query
import dns.zone

domain = 'amarelo.dojo'
target = 'ns.yellow.dojo'

try:
    transfzone = dns.zone.from_xfr(dns.query.xfr(target, domain))

    for _maquinas in transfzone:
        print('[+] - ', str(_maquinas) + '.' + domain)

except:
    print('[+] - Falha na transferência de zona do domínio:', domain, 'NS:', target)
