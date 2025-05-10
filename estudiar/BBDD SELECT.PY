import sqlite3

miConexion=sqlite3.connect("PrimeraBD")

miCursor=miConexion.cursor()

miCursor.execute("SELECT * FROM PRDUCTOS")

variosProdcutos=miCursor.fetchall()

for i in variosProdcutos:
       print("Nombre del Articilo", i[0], "seccion:",i[2], "PRECIO:",i[1])


miConexion.commit()

miConexion.close()