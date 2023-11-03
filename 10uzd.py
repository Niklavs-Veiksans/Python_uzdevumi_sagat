"""
Izmantojot map() funkciju izveidot no diviem sarakstiem saliktnei.


"""
saraksts1 = ["skapis", "debess", "vējš", "mežģīne"]
saraksts2 = ["ledus", "koks", "ceļš", "mežs"]

saliktenis = list(map(lambda x, y: y + x, saraksts1, saraksts2))
print(saliktenis)