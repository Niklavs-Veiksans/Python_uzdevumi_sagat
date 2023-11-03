"""
Uzrakstiet Python programmu, lai trīskāršotu visus dotā veselo skaitļu saraksta skaitļus.
Izmantojiet Python map() funkciju.
"""


saraksts = [1, 2, 3, 4, 5]


def triskarsot(skaitlis):
    return skaitlis * 3


trisk = list(map(triskarsot, saraksts))


print("saksk:", saraksts)
print("trissk:", trisk)