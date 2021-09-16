#!/usr/bin/python
import nmap3
from datetime import datetime
from termcolor import colored

msg1 = colored('+', 'green', attrs=['blink'])
msg2 = colored('+', 'cyan')
msg3 = colored('->', 'cyan')
nmap_start = datetime.now()

target = '11.11.11.171'

pynmap = nmap3.NmapScanTechniques()
finscan = pynmap.nmap_fin_scan(target)


print('[' + msg1 + '] Porta:', finscan['ports']['portid'])
print('[' + msg1 + '] Protocolo:', finscan['ports']['protocol'])
print('[' + msg1 + '] Serviço:', finscan['ports']['service']['name'])
print('[' + msg1 + '] Estado:', finscan['ports']['state']['state'])

    
nmap_end = datetime.now()
nmap_time = nmap_end - nmap_start
print('[' + msg1 + ']', 'Tempo de execução:', nmap_time)

print()

