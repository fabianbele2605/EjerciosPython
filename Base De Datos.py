import sqlite3

miConexion=sqlite3.connect("PrimeraBD")

miCursor=miConexion.cursor()

miCursor.execute(
     TABLE PRODUCTOR (
     CODIGO INTERGER PRIMARY KEY AUTOINCREMENT,
     NOMBRE VARCHAR(50),
     PRECIO INTEGER(10),
     SECCION VARCHAR(20))
)

productos=[
    ("Pelota",3500,"Jugueteria"),
    ("Pantalon",39990,"Textil"),
    ("Destormillador",1500,"Ferreria"),
    ("Jarron",2000,"Menaje"),
]

miCursor.executemany("INSERT INTO PRODUCTOR VALUES (NULL,?,?,?)", productos)


miConexion.commit()

miConexion.close()

