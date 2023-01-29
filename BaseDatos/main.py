import mysql.connector

#Mi primera conexión
database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Nagashandrex9",
    database = "coltis_python"
)

#try:
#    print(f"Se conecto!! : {database} ")
#except:
#    print("Ha fallado la conexión")    

# try:
#     cursor =database.cursor()
#     cursor.execute("CREATE DATABASE IF NOT EXISTS coltis_python")
#     cursor.execute("SHOW DATABASES")
    
#     for basesDatos in cursor:
#         print(basesDatos)
        
    
    #print("Base de datos creada")--una ves comprobada la creación de la bd, ya no se necesita este print
# except:
#     print("La creación de la base de datos ha fallado")
#DEPUES DE QUE NOS MOSTRO LAS BASES DE DATOS QUE TENEMOS Y SE CREO LA NUESTRA YA PODEMOS BORRAR EL TRY Y EL EXCEPT 

cursor = database.cursor(buffered=True)

# try:
#     cursor.execute("""
#     CREATE TABLE IF NOT EXISTS estudiante (
#         id int (12) auto_increment not null,
#         nombre varchar (55) not null,
#         apellidos varchar (12) not null,
#         celular varchar(12) not null,
#         CONSTRAINT pk_estudiante PRIMARY KEY (id)
#     )
                
#                 """
#                 )
#     print("Funcionando")

# except:
#     print("Error al crear la tabla")
#DEPUES DE CREAR LA TABLA ESTUDIANTE  YA PODEMOS BORRAR EL TRY Y EL EXCEPT 

# try: 
#     cursor.execute("INSERT INTO estudiante VALUES (null, 'Andrés', 'Baldión', '000000000' )")
#     cursor.execute("commit")
#     print("Dato Guardado")

# except:
#     print("Ha fallado el guardar")

# try:
#     estudiantes = [
#         ('Tito', 'Rubio', '123445'),
#         ('Tony', 'stark', '156622'),
#         ('juan', 'dante', '000222')
#     ]
#     cursor.executemany("INSERT INTO estudiante VALUES (null, %s, %s, %s)", estudiantes)
#     cursor.execute("commit")
#     print("datos guardados")
# except:
#     print("Ha fallado el guardar")

# try:
#     cursor.execute("SELECT * FROM estudiante")
    
#     result = cursor.fetchall()
    
#     print("Estudiantes")
#     for estudiantes in result:
#         print(estudiantes)
# except:
#     print("Fallo de consulta")         
    

# try:
#     cursor.execute("DELETE FROM estudiante WHERE id = 5")
#     database.commit()
#     print("Eliminación exitosa")
# except:
#     print("Fallo de eliminación") 
    
try:
    cursor.execute("UPDATE estudiante SET apellidos = 'González' WHERE id = 7")
    database.commit()
    print("Actualización exitosa")
except:
    print("Fallo de actualización")   

      




