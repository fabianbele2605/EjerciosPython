import sqlite3

miConexion=sqlite3.connect("PrimeraBD")

miCursor=miConexion.cursor()

variosArticulos=[

     ("CAMISETAS", 19000, "DEPORTES"),
     ("PERNOS", 100, "FERRETERIA"),
     ("PERFUMES", 12000, "PERFUMERIAS"),

]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)",variosArticulos)


miConexion.commit()

miConexion.close()

