#! /usr/bin/python

import argparse
import whois

msg_usage = "\n Utilize desta forma: ./whois_004.py -d <dominio alvo> \n"
msg_domain = "Informe o dominio alvo com -d ou --domain"

def func_whois(_domain):
    querywhois = whois.query(_domain)
    print("Nome do domínio: ", querywhois.name)
    print("Data de criação: ", querywhois.creation_date)
    print("Data de expiração: ", querywhois.expiration_date)
    print("Data de última atualização: ", querywhois.last_updated)
    print("Servidor WHOIS registrado: ", querywhois.registrar)
    
    for _domain in querywhois.name_servers:
        print("Servidor de nomes: ", _domain)

def func_main():
    option = argparse.ArgumentParser(description=msg_usage)
    option.add_argument("-d", "--domain", action="store", dest="domain", help=msg_domain)
    option_args = option.parse_args()

    if option_args.domain == None:
        print(option.description)

    domaintarget = option_args.domain
    func_whois(domaintarget)

if __name__ == '__main__':
    func_main()

