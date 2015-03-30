#!/usr/bin/python

#name = raw_input("Enter file:")
#if len(name) < 1 : name = "mbox-short.txt"
name = "code/mbox-short.txt"
handle = open(name)
exit()
Dict = dict()
for line in handle:
    if not line.startswith('From '): continue
    email = line.split()[1]
    Dict[email] = Dict.get(email, 1) + 1
gratest = sorted(Dict, key=Dict.get, reverse=True)[0]
print(gratest + ' ' + str(Dict[gratest]))
