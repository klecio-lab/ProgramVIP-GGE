# coding=<UTF-8>
#em pynput, importar o método Listener do teclado
from pynput.keyboard import Listener
import pyautogui
from PIL import ImageGrab
import time
from datetime import datetime, timedelta
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
    print("conexão não foi possivel, linha 21")

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
                vel = float(0.25)
                cont = 0
                cont2 = 0

                vel = 0.25
                G_eventos = (681,502)
                confirmar = (110, 172, 27)
                smoke = (196, 197, 176)
                smoke2 = (225, 220, 216)
                smoke3 = (202, 200, 180)
                smoke4 = (205, 201, 199)
                smoke5 = (204, 200, 198)

                def avancar():
                    #clicar no alvo
                    pyautogui.click(838,569, interval=0.25)
                    #clicar no alvo
                    pyautogui.click(838,569, interval=0.25)
                    #clicar no botão de atacar
                    pyautogui.click(892,570, interval=vel)
                    #clicar no botão de avamço
                    pyautogui.click(830,367, interval=vel)
                    #clicar no avanço de 1 hora
                    pyautogui.click(620,407, interval=vel)
                    #clicar na seta para esquerda
                    pyautogui.click(447,408, interval=vel)
                    #clicar no avanço de meia hora
                    pyautogui.click(617,409, interval=vel)
                    #clicar no X
                    pyautogui.click(579,514, interval=vel)
                    

                def coletar():
                    #clicar no alvo
                    pyautogui.click(681,502, interval=0.25)

                def detectar_cor():
                    screen = ImageGrab.grab()
                    color = screen.getpixel((819,462))
                    color2 = screen.getpixel(G_eventos)
                    #print(color)
                    
                    if color == smoke or color == smoke2:
                        avancar()
                    if color == smoke3 or color == smoke4: 
                        avancar()
                    if color == smoke5:
                        avancar()
                    if color2 == confirmar:
                        coletar()

                def calcular_tempo():
                    #pegando hora atual
                    nova_hora = datetime.now()
                    hora_atual = nova_hora.strftime('%H:%M:%S')

                    return hora_atual
                    
                def calcular_tempoPrevisto():
                    #pegando hora atual
                    nova_hora = datetime.now()
                    hora_atual = nova_hora.strftime('%H:%M:%S')
                    #adicionado a hora atual a quantidade de minutos
                    td = timedelta(seconds=10)   
                    hora_prevista = nova_hora + td
                    TempoParar = hora_prevista.strftime('%H:%M:%S')

                    return TempoParar
                    

                def writeLog(key):

                    #dicionário com as teclas a serem traduzidas
                    translate_keys = {
                        "Key.space": " ",
                        "Key.shift_r": "",
                        "Key.shift_l": "",
                        "Key.enter": "\n",
                        "Key.alt": "",
                        "Key.esc": "esc",
                        "Key.cmd": "",
                        "Key.caps_lock": "",
                    }

                    #converter a tecla pressionada para string
                    keydata = str(key)

                    #remover as asplas simples que delimitam os caracteres
                    keydata = keydata.replace("'", "")

                    for key in translate_keys:
                        #key recebe a chave do dicionário translate_keys
                        #substituir a chave (key) pelo seu valor (translate_keys[key])
                        keydata = keydata.replace(key, translate_keys[key])

                    texto = str(keydata)
                        
                    
                    
                    #Para Nomades ou samurais
                    if texto == "Key.f9":
                        cont = 0
                        while(cont != 1):
                            time.sleep(vel)
                            #clicar no alvo
                            pyautogui.click(838,569, interval=vel)
                            #clicar no alvo
                            pyautogui.click(838,569, interval=vel)
                            #clicar no botão de atacar
                            pyautogui.click(892,570, interval=vel)
                            #clicar no botão de confirmar ataque
                            pyautogui.click(769, 515, interval=vel)
                            #tempo pra carregar menu de ataque
                            time.sleep(1)

                            #----------------------------------

                            #clicar no botão de ondas
                            pyautogui.click(451, 650, interval=vel)
                            #selecionar predefinição da 3 onda
                            pyautogui.click(332, 605, interval=vel)
                            #clicar no botão atualizar todas as ondas
                            pyautogui.click(543, 652, interval=vel)
                            #clicar no botão de ondas
                            pyautogui.click(451, 650, interval=vel)
                            #selecionar a 1 onda
                            pyautogui.click(338,637, interval=vel)
                            #atualizar 1 onda
                            pyautogui.click(513, 653, interval=vel)
                            #passar pra 2 onda
                            pyautogui.click(557, 615, interval=vel)
                            #clicar no botão de ondas
                            pyautogui.click(451, 650, interval=vel)
                            #selecionar predefinição da 2 onda
                            pyautogui.click(333,622, interval=vel)
                            #atualizar 2 onda
                            pyautogui.click(513, 652, interval=vel)

                            #----------------------------------

                            #clicar no botão atacar
                            pyautogui.click(996, 694, interval=vel)
                            #clicar no botão de cavalo
                            pyautogui.click(495, 413, interval=vel)
                            #clicar no botão de mandar ataque
                            pyautogui.click(799, 593, interval=vel)
                            cont += 1

                        horaObjetivo = str(calcular_tempoPrevisto())
                        horaAgora = str(calcular_tempo())
                        while horaObjetivo != horaAgora:
                            detectar_cor()
                            horaAgora = str(calcular_tempo())
                            print(horaAgora)


                #abrir o Listener do teclado e escutar o evento on_press
                #quando o evento on_press ocorrer, chamar a função writeLog  
                with Listener(on_press=writeLog) as l:
                    l.join()
'''
else:
    quit()
'''
