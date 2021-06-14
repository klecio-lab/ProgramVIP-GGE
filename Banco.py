import pymysql  # conectar com o bd

# criando conexão com o servidor
try:
    conexao = pymysql.connect(
        host='us-cdbr-east-04.cleardb.com',
        user='b4008aac54e85f',
        password='6745c2c0',
        database='heroku_33ce7bcefe3dfe5'
    )
except pymysql.err.OperationalError:
    print("conexão não foi possivel, linha 20")
    
cursor = conexao.cursor()

#CRIAR TABELAS
#cursor.execute("CREATE TABLE Clientes(id INT AUTO_INCREMENT PRIMARY KEY, usuario VARCHAR(50), senha VARCHAR(50))")

#mostrar tabelas
'''
cursor.execute("SHOW TABLES;")

for var01 in cursor:
    print(var01)
'''

#adicionar novos usuarios
'''
com_sql = "INSERT INTO Clientes(usuario,senha,nomepc) VALUES (%s,%s,%s)"
valor = ("João","2244","LAPTOP-C4A0Q21L")

cursor.execute(com_sql,valor)

#gravar permanente as alterações
conexao.commit()

#quantas linhas foram adicionadas 
print(cursor.rowcount)
'''

#COMANDO SELECT

cursor.execute("SELECT * FROM Clientes WHERE usuario = 'João'")

resultado = cursor.fetchall()

for x in resultado:
    print(x)


#COMANDO DELETE
'''
com_slq = "DROP TABLE Clientes"

cursor.execute(com_slq)

conexao.commit()

print(cursor.rowcount)
'''

#COMANDO ALTER TABLE USADO PARA ALTERAR BANCOS E TABELAS
'''
com_slq = "ALTER TABLE Clientes ADD nomepc VARCHAR(50)"

cursor.execute(com_slq)

conexao.commit()

print(cursor.rowcount)
'''

