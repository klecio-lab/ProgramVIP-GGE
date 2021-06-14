# coding=<UTF-8>
#em pynput, importar o método Listener do teclado
from pynput.keyboard import Listener
import pyautogui
import time
from PIL import ImageGrab
from datetime import datetime, timedelta
import platform
from pymsgbox import *



plataforma = str(platform.node())
if plataforma == 'DESKTOP-2J57S36':

    print("platadorma aceita")
    alert(text='Programa iniciado com sucesso', title='Iniciado', button='OK')

    vel = float(0.25)
    cont = 0
    cont2 = 0
    G_eventos = (681,502)
    confirmar = (110, 172, 27)
    smoke = (196, 197, 176)
    smoke2 = (225, 220, 216)
    smoke3 = (202, 200, 180)
    smoke4 = (205, 201, 199)
    smoke5 = (204, 200, 198)
    vel = float(0.25)
    cont = 0
    cont2 = 0

    def avancar():
        #clicar no alvo
        pyautogui.click(703,492, interval=0.5)
        #clicar no alvo
        pyautogui.click(703,492, interval=0.5)
        #clicar no botão de atacar
        pyautogui.click(756,492, interval=vel)
        #clicar no botão de avamço
        pyautogui.click(830,367, interval=vel)
        #clicar no avanço de 1 hora
        pyautogui.click(620,407, interval=vel)
        #clicar na seta para esquerda
        pyautogui.click(447,408, interval=vel)
        #clicar no avanço de meia hora
        pyautogui.click(617,409, interval=vel)
        #fechar tela de ataque
        pyautogui.click(577,527, interval=vel)

    def coletar():
        #clicar no alvo
        pyautogui.click(681,502, interval=0.25)

    def detectar_cor():
        screen = ImageGrab.grab()
        color = screen.getpixel((683, 384))
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
        td = timedelta(minutes=3)   
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
            while cont !=  35:
            
                time.sleep(vel)
                #clicar no alvo
                pyautogui.click(703,492, interval=vel)
                #clicar no alvo
                pyautogui.click(703,492, interval=vel)
                #clicar no botão de atacar
                pyautogui.click(756,492, interval=vel)
                #clicar no botão de confirmar ataque
                pyautogui.click(769, 515, interval=vel)
                #tempo pra carregar menu de ataque
                time.sleep(1)
                
                #----------------------------------

                #clicar no botão de atualizar onda para ter bau em tudo
                pyautogui.click(544,650, interval=vel)
                #clicar no bau
                pyautogui.click(646,408, interval=vel)
                #clicar no retirar o bau
                pyautogui.click(816,201, interval=vel)
                #clicar no botão de automatico
                pyautogui.click(910,694, interval=vel)

                #----------------------------------
                
                #clicar no botão atacar
                pyautogui.click(996, 694, interval=vel)
                #clicar no botão de cavalo
                #pyautogui.click(495, 413, interval=vel)
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
else:
    quit()


