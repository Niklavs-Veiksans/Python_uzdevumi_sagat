"""
Uzrakstiet Python programmu, lai diviem sarakstiem noteikti atšķirību.
Izmantojiet funkciju map().
"""

# Dotie saraksti
saraksts1 = [1, 2, 3, 4, 5]
saraksts2 = [3, 4, 5, 6, 7]

# Izmantojam filter() un lambda funkciju, lai atrastu atšķirīgos elementus
atšķirīgie_elementi = list(filter(lambda x: x not in saraksts2, saraksts1))

# Izdrukājam rezultātu
print("Saraksts 1:", saraksts1)
print("Saraksts 2:", saraksts2)
print("Atšķirīgie elementi:", atšķirīgie_elementi)
