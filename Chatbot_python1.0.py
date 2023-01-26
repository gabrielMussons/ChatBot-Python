
import pyautogui as bot
from time import sleep
import pyperclip as clip
from PIL import Image
import random
import cv2

img = cv2.imread(r'C:\Users\Gabriel\Desktop\notificacion.png') 

sleep(5)

def obtenerMensaje():
    bot.moveTo(508,628)
    bot.tripleClick()
    bot.hotkey('ctrl','c')
    msj=clip.paste()
    bot.click()
    print('Mensaje recibido:',msj)
    return msj


def limpiarMensaje(msj):
    vocales=['a','e','i','o','u']

    for index, item in enumerate(['á','é','í','ó','ú']):
        if item in msj :
            clean_txt= msj.replace(item,vocales[index])
        else:
            clean_txt=msj
    return clean_txt

def procesarMensaje(msj):
    mensaje= msj.lower()

    print('mensaje minuscula:',mensaje)

    mensaje= limpiarMensaje(mensaje)

    print('mensaje sin acentos:', mensaje)

    if mensaje == 'hola':
        respuestas= ['Hola como estas?','Holaa como le va ?','holi que tal','holardo como ta tu', 'ciao bella']
        r = random.choice(respuestas)
        clip.copy(r)
        print('respuesta',r)
    


def pegarRespuesta():
    bot.moveTo(530,695)
    bot.click()
    bot.hotkey('ctrl','v')
    bot.hotkey('enter')


def revisarNotificaciones():
    sleep(5)

    px_white=(503,641)
    bot.moveTo(px_white)
    
    try:
        cordenadas = bot.locateCenterOnScreen(img, confidence = 0.7)
        bot.moveTo(cordenadas)
        bot.moveRel(-150,0)
        bot.click()
        sleep(2)
    except:
        pass

    try:
        if bot.pixelMatchesColor(px_white[0],px_white[1],(255,255,255),tolerance=10):
            print('Nuevo mensaje')
            procesarMensaje(obtenerMensaje())
            pegarRespuesta()
        else:
            sleep(1)
    except(Exception):
        pass


revisarNotificaciones()