#!/usr/bin/python

import dns.resolver
myquery = dns.resolver.Resolver()
domain = "yahoo.com"
host = "www"
target = host + "." + domain

def func_aaaa(_target):
    question = myquery.query(_target, 'AAAA')

    for _aaaa in question:
        print(_aaaa)

func_aaaa(target)        
