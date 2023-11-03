"""
Papildināt programmu ar ciklu, kurā sarakstā esošiem uzvārdiem tiktu 
pievienots klāt doktora nosaukums - Dr.
"""


saraksts1 = ["Kalniņš", "Opmanis", "Vēzis", "Almane"]
saraksts2 = []

for uzv in saraksts1:
    doktors_uzv = "Dr. " + uzv
    saraksts2.append(doktors_uzv)

print(saraksts2)