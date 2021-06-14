from datetime import datetime, timedelta

'''
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
    
a = calcular_tempo()
b = calcular_tempoPrevisto()'''

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
    
horaObjetivo = str(calcular_tempoPrevisto())
horaAgora = str(calcular_tempo())
while horaObjetivo != horaAgora:
    horaAgora = str(calcular_tempo())
    print(horaAgora)
    print(horaObjetivo)
    
