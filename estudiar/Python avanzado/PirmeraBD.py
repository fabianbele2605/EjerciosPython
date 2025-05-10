import sqlite3

miConexion=sqlite3.connect("PrimeraBD")

miCursor=miConexion.cursor()

miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULOS VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")

miConexion.close()

