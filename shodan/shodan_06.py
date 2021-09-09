#!/usr/bin/python

import shodan
shodan_mykey = 'dTNGRiwYNozXIDRf5DWyGNbkdiS5m3JK'
shodan_api = shodan.Shodan(shodan_mykey)
shodan_target = '179.191.78.194'
shodan_host = shodan_api.host(shodan_target)

def shodan_info():
    print('[*] Informações genéricas do ALVO','\n')
    print('[+] - IP alvo:', shodan_host['ip_str'])
    print('[+] - Organizacao:', shodan_host.get('org', 'n/a'))
    print('[+] - Sistema Operacional:', shodan_host.get('os', 'n/a'))

def shodan_portscan():
    print('[*] Identificação de portas abertas','\n')

    for _line in shodan_host['data']:
        print("[+] - Porta aberta:", _line['port'])
        print("[+] - Banner:", _line['data'])

def shodan_vuln():
    print('[*] Lista de possíveis Vulnerabilidades CVE','\n')

    for _item in shodan_host['vulns']:
        CVE = _item.replace('!','')
        print('[+] - Vulnerability:', _item)

print('\n','-' * 60,'\n')
shodan_info()
print('\n','-' * 60,'\n')
shodan_portscan()
print('\n','-' * 60,'\n')
shodan_vuln()
print('\n','-' * 60,'\n')
