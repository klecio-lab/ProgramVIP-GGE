from PySimpleGUI import PySimpleGUI as sg
import pymysql  # conectar com o bd
import platform

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


sg.theme('DarkAmber')
layout = [
    [sg.Text('ID:'), sg.Input(key='id', size=(5, 1))],
    [sg.Text('Usuário:'), sg.Input(key='usuario', size=(20, 1))],
    [sg.Text('Senha:  '), sg.Input(key='senha', size=(20, 1), password_char='*')],
    [sg.Button('Entrar')]
]

janela = sg.Window('Tela de Login', layout)
    
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    #parte de verificação de user
    if eventos == 'Entrar':

        PegarID = valores['id']
        ComandoUsuario = "SELECT * FROM Clientes WHERE id = " + PegarID
        #PegarUsuario = str(valores['usuario'])
        #ComandoUsuario = "SELECT * FROM Clientes WHERE id = " + "\'" + PegarUsuario + "\'"
        cursor.execute(ComandoUsuario)
        resultado = cursor.fetchall()
        for Nome in resultado:
            Nome = Nome

        if valores['usuario'] in Nome and valores['senha'] in Nome:
            print("bem vindo ao algoritmo")
            plataforma = str(platform.node())
            if plataforma in Nome:
                print("plataforma aceita")
