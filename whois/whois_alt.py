#! /usr/bin/python

import whois

target = "uol.com.br"

def func_whois(_domain):
    querywhois = whois.query(_domain)
    print("Nome do domínio: ", querywhois.name)
    print("Data de criação: ", querywhois.creation_date)
    print("Data de expiração: ", querywhois.expiration_date)
    print("Data de última atualização: ", querywhois.last_updated)
    print("Servidor WHOIS registrado: ", querywhois.registrar)
   
    print(" ")

    for _domain in querywhois.name_servers:
        print("Servidor de nomes: ", _domain)


func_whois(target)

