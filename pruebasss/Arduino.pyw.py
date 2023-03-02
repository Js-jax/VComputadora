import tkinter as tk
from tkinter import ttk
from tkinter import *# declaracion de  la libreria tkinter
import serial, time #librerial para la comunicacion de arduino 
raiz=Tk()# declaracion de la clase tkinter
raiz.title('TELEMETRIA')#ingresar el titulo de la interfaz
raiz.geometry('1366x768')# dimenciones de la pantalla
#raiz.config(bg="black")

def temperaturaa():
 print('Button clicked')
 tempe=Tk()
 tempe.title("TEMPERATURA")
 tempe.mainloop()
def humeee():
 print('Button clicked')
 hume=Tk()
 hume.title("HUMEDAD")
 hume.mainloop()
def Auu():
 print('Button clicked')
 audi=Tk()
 audi.title("AUDIO")
 audi.mainloop()
def videe():
 print('Button clicked')
 vide=Tk()
 vide.title("VIDEO")
 vide.mainloop()
def ubiii():
  print('Button clicked')
  ubi=Tk()
  ubi.title("UBICACION")
  ubi.mainloop()
def call():
    print('Button clicked')
    cal=Tk()
    cal.title("CALOR")
    cal.mainloop()


salir_boton=Button(raiz,text='hola',command=lambda:raiz.quit(),bg="#FFA500")
salir_boton.pack(ipadx=1,ipady=1,)
temperatura=ttk.Button(raiz ,text='temperatura',command=temperaturaa)
temperatura.place(x=10, y=100)
humedad=ttk.Button(raiz ,text='humedad', command=humeee)
humedad.place(x=100, y=100)
audio=ttk.Button(raiz ,text='audio',command=Auu)
audio.place(x=180, y=100)
video=ttk.Button(raiz ,text='video',command=videe)
video.place(x=240, y=100)
ubicacion=ttk.Button(raiz ,text='ubicacion',command=ubiii)
ubicacion.place(x=300, y=100)
calor=ttk.Button(raiz ,text='calor',command=call)
calor.place(x=370, y=100)



mensaje =Label(raiz, text="-----Bienvenido al menu de telemetria--------")#mesnaje a guardar y posterior a mostrar
mensaje.pack()#mostrar en pantalla el mensaje   que se guardo arriba 
raiz.mainloop()#abrir pantalla  ventana emergente 



arduino = serial.Serial('COM5',9600)#selecciona en que puerto esta comunicando el arduino
time.sleep(1)
Datos = arduino.readline()#se guardan los datos que se estan mandando  desde la pantalla serial  y se guardan en datos 
while 1:#se genera un bucle while para repetir todo  el proceso 
 COMM=(print(Datos.decode('utf-8')) )# se manda a imprimir en pantalla los datos que se le estan mandando 
 time.sleep(1)# es el tiempo de envio de datos  en el momento de transmitirnos 


