# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 11:25:02 2022

@author: j_dbg
"""

from BarraSencilla import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo
import PIL.Image
import PIL.ImageTk

adyet={}
botonseccsup={}
botonInterruptor={}
botonseccinf={}
adybt={}
botonVeri={}
label={}

raiz=Tk()
raiz.title("Simulador Barra Sencilla")
capap=Frame(raiz,bg="#F1ECEB",width=500,height=500)
capa1=Frame(capap,bg="#FFFF00",width=200, height=200,relief="sunken",borderwidth=3)
capa2=Frame(capap,bg="black",width=200, height=200,relief="sunken",borderwidth=3)
capa3=Frame(capap,bg="#000F00",width=200, height=200,relief="sunken",borderwidth=3)
capa4=Frame(capap,bg="black",width=200, height=200,relief="sunken",borderwidth=3)
canvas2=Canvas(capa2,bg='white')
canvas3=Canvas(capa4,bg="white")
text=Text(canvas3,width=25,height=23)
campos = askstring('Campos', 'Cuantos Campos quiere')
if campos:
    if campos.isdigit():
        campos=int(campos)
    else:
        messagebox.showinfo(message="Debe ingresar numeros", title="Estado")
        raiz.destroy()
else:
    raiz.destroy()
prueba=barraSencilla(campos)
altura=0
ancho=0
if prueba.campos%2==0:
    ancho=prueba.campos/2
else:
    ancho=(prueba.campos+1)/2
Frame1=Frame(canvas2,bg='white', width=(110*ancho)+40, height=400)
scrollCapa2=Scrollbar(capa2,orient="vertical",command=canvas2.yview)
scrollxCapa2=Scrollbar(capa2, orient="horizontal",command=canvas2.xview)
####Se expande con Grid la ventana raiz o root
raiz.rowconfigure(0, weight=1)
raiz.columnconfigure(0, weight=1)
###Se aplica la propiedad de expandirse a la capa1 
capap.grid(sticky=NSEW)
capap.grid_columnconfigure(1, weight=1)
capap.grid_rowconfigure(0, weight=1)
capap.grid_rowconfigure(1, weight=1)
###Se configura Scroll
scrollCapa2.pack(side=RIGHT,fill=Y)
scrollxCapa2.pack(side=BOTTOM,fill=X)
canvas2.configure(yscrollcommand=scrollCapa2.set, xscrollcommand=scrollxCapa2.set)
canvas2.bind('<Configure>', lambda e: canvas2.configure(scrollregion= canvas2.bbox("all")))
###----------------------------------------------------------------------------------------
scrollCapa4=Scrollbar(capa4,orient="vertical",command=text.yview)
scrollxCapa4=Scrollbar(capa4, orient="horizontal",command=text.xview)
scrollCapa4.pack(side=RIGHT,fill=Y)
scrollxCapa4.pack(side=BOTTOM,fill=X)
text.configure(yscrollcommand=scrollCapa4.set, xscrollcommand=scrollxCapa4.set)
text.bind('<Configure>', lambda e: text.configure(scrollregion= text.bbox("all")))
###------------###----------------###---------------###--------------###---------------
canvas2.pack(fill=BOTH,expand=1)
canvas3.pack(fill=BOTH,expand=1)
text.grid(row=0,column=0)
##Se ubica Capa 2 y capa 3
canvas2.create_window((0,0), window=Frame1, anchor='nw')
capa1.grid(row=0, rowspan=2,column=0,padx=(10,10),pady=(10,10),sticky=NSEW)
capa2.grid(row=0, rowspan=2,column=1,padx=(10,10),pady=(10,10),sticky=NSEW)
capa3.grid(row=0, column=2,padx=(10,10),pady=(10,10),sticky='EWNS')
capa4.grid(row=1, column=2,padx=(10,10),pady=(10,10),sticky='EWNS')

barraPrincipal=Label(Frame1, bg="black", bd=3, relief="ridge" )
barraPrincipal.place(x=20,y=190,width=110*ancho,height=20)
#-----------------------------------------Imagenes---------------------------------------------------------
#-------------------Adyacente Barra Impar------------------------------
sabi = PIL.Image.open("imagenes/SeccAdyaBarImpar.png")
sabi = PIL.ImageTk.PhotoImage(sabi.resize((50,50),PIL.Image.ANTIALIAS))
#-------------------Adyacente Barra Par--------------------------------
sabp = PIL.Image.open("imagenes/SeccAdyaBarPar.png")
sabp = PIL.ImageTk.PhotoImage(sabp.resize((50,50),PIL.Image.ANTIALIAS))
#-------------------InterruptorAbierto---------------------------------
intea = PIL.Image.open("imagenes/InterruptorAbierto.png")
intea = PIL.ImageTk.PhotoImage(intea.resize((50,50),PIL.Image.ANTIALIAS))
#-------------------InterruptorCerrado---------------------------------
intec = PIL.Image.open("imagenes/InterruptorCerrado.png")
intec = PIL.ImageTk.PhotoImage(intec.resize((50,50),PIL.Image.ANTIALIAS))
#-------------------InterruptorCerradoEnergizado---------------------------------
intece = PIL.Image.open("imagenes/InterruptorCerradoEnergizado.png")
intece = PIL.ImageTk.PhotoImage(intece.resize((50,50),PIL.Image.ANTIALIAS))
#-------------------SeccAdyaBarImparBar1Est1---------------------------------
sabic = PIL.Image.open("imagenes/SeccAdyaBarImparBar1Est1.png")
sabic = PIL.ImageTk.PhotoImage(sabic.resize((50,50),PIL.Image.ANTIALIAS))
#-------------------VerficacionOk---------------------------------
ver = PIL.Image.open("imagenes/VerficacionOk.png")
ver = PIL.ImageTk.PhotoImage(ver.resize((50,50),PIL.Image.ANTIALIAS))
#-----------------------------------------------------------------------------
si1e0 = PIL.Image.open("imagenes/SeccAdyaBarImparBar0Est1.png")
si1e0 = PIL.ImageTk.PhotoImage(si1e0.resize((50,50),PIL.Image.ANTIALIAS))

pasos=""

correr=0
for c in range(prueba.campos):
    x=c+1
    if x%2==0:
        correr=((((x)/2)-1)*110)
        adyet["int"+str(c+1)]=Label(Frame1, bg='green', bd=3,relief="ridge")
        botonseccsup["int"+str(c+1)]=Button(Frame1,text="SS "+ str(c+1), command=lambda x=x : accionSecSuperior(x),image=sabi)
        botonInterruptor["int"+str(c+1)]=Button(Frame1,text="I "+ str(c+1),command=lambda x=x : accionInterruptor(x),image=intea)
        botonVeri["int"+str(c+1)]=Button(Frame1,bg="black",command=lambda x=x : verificarSincronismo(x))
        botonseccinf["int"+str(c+1)]=Button(Frame1,text="SI"+ str(c+1),command=lambda x=x : accionSecInferior(x),image=sabp)
        adybt["int"+str(c+1)]=Label(Frame1, bg='black', bd=3,relief="ridge")
        #----------------Labels--------------------------------------
        label["SS"+str(c+1)]=Label(Frame1,bg="white", text="L"+str(c+1)+"3")
        label["I"+str(c+1)]=Label(Frame1,bg="white", text="L"+str(c+1)+"0")
        label["VS"+str(c+1)]=Label(Frame1,bg="white", text="Ver L"+str(c+1)+"0")
        label["SI"+str(c+1)]=Label(Frame1,bg="white", text="L"+str(c+1)+"5")
        #----------------Posicion Botones-------------------------------------
        adyet["int"+str(c+1)].place(x=55+correr,y=380,width=20 ,height=20)
        botonseccsup["int"+str(c+1)].place(x=40+correr, y=330,width=50,height=50)
        botonInterruptor["int"+str(c+1)].place(x=40+correr,y=280,width=50,height=50)
        botonVeri["int"+str(c+1)].place(x=90+correr,y=280,width=10,height=50)
        botonseccinf["int"+str(c+1)].place(x=40+correr,y=230,width=50,height=50)
        adybt["int"+str(c+1)].place(x=55+correr,y=210,width=20 ,height=20)
        #----------------Posicion Labels-------------------------------------
        label["SS"+str(c+1)].place(x=90+correr, y=330,width=50,height=50)
        label["I"+str(c+1)].place(x=100+correr,y=280,width=40,height=25)
        label["VS"+str(c+1)].place(x=100+correr,y=305,width=40,height=25)
        label["SI"+str(c+1)].place(x=90+correr,y=230,width=50,height=50)
    else:
        correr=((((x+1)/2)-1)*110)
        adyet["int"+str(c+1)]=Label(Frame1, bg='green', bd=3,relief="ridge")
        botonseccsup["int"+str(c+1)]=Button(Frame1,text="SS "+ str(c+1),command=lambda x=x : accionSecSuperior(x),image=sabp)
        botonInterruptor["int"+str(c+1)]=Button(Frame1,text="I "+ str(c+1), command=lambda x=x : accionInterruptor(x),image=intea)
        botonVeri["int"+str(c+1)]=Button(Frame1,bg="black",command=lambda x=x : verificarSincronismo(x))
        botonseccinf["int"+str(c+1)]=Button(Frame1,text="SI"+ str(c+1),command=lambda x=x : accionSecInferior(x),image=sabp)
        adybt["int"+str(c+1)]=Label(Frame1, bg='black', bd=3,relief="ridge")
        #----------------Labels--------------------------------------
        label["SS"+str(c+1)]=Label(Frame1,bg="white", text="L"+str(c+1)+"3")
        label["I"+str(c+1)]=Label(Frame1,bg="white", text="L"+str(c+1)+"0")
        label["VS"+str(c+1)]=Label(Frame1,bg="white", text="Ver L"+str(c+1)+"0")
        label["SI"+str(c+1)]=Label(Frame1,bg="white", text="L"+str(c+1)+"5")
        #----------------Posicion Botones-------------------------------------
        adyet["int"+str(c+1)].place(x=55+correr,y=0,width=20 ,height=20)
        botonseccsup["int"+str(c+1)].place(x=40+correr, y=20,width=50,height=50)
        botonInterruptor["int"+str(c+1)].place(x=40+correr,y=70,width=50,height=50)
        botonVeri["int"+str(c+1)].place(x=90+correr,y=70,width=10,height=50)
        botonseccinf["int"+str(c+1)].place(x=40+correr,y=120,width=50,height=50)
        adybt["int"+str(c+1)].place(x=55+correr,y=170,width=20 ,height=20)
        #----------------Posicion Labels-------------------------------------
        label["SS"+str(c+1)].place(x=90+correr, y=20,width=50,height=50)
        label["I"+str(c+1)].place(x=100+correr,y=70,width=40,height=25)
        label["VS"+str(c+1)].place(x=100+correr,y=95,width=40,height=25)
        label["SI"+str(c+1)].place(x=90+correr,y=120,width=50,height=50)
def accionInterruptor(campo):
    
    messagebox.showinfo(message=prueba.accionInterruptor(campo), title="Estado")
    if prueba.i["I"+str(campo)]:
        botonInterruptor["int"+str(campo)].configure(image=intece)
        botonVeri["int"+str(campo)].configure(bg="green")
    else:
        botonInterruptor["int"+str(campo)].configure(image=intea)
    text.insert(END,"\n L"+str(campo)+"0 estado "+ str(prueba.i["I"+str(campo)]))
    estadoBarraPrincipal()
    
def accionSecSuperior(campo):
    
    messagebox.showinfo(message=prueba.accionSecSuperior(campo), title="Estado")
    if prueba.ss["SS"+str(campo)]:
        botonseccsup["int"+str(campo)].configure(image=sabic)
    else:
        if campo%2==0:
            botonseccsup["int"+str(campo)].configure(image=sabi)
        else:
            botonseccsup["int"+str(campo)].configure(image=sabp)
    text.insert(END,"\n L"+str(campo)+"3 estado "+ str(prueba.ss["SS"+str(campo)]))
    
def accionSecInferior(campo):
    
    messagebox.showinfo(message=prueba.accionSecInferior(campo), title="Estado")
    if prueba.si["SI"+str(campo)]:
        if prueba.barraPrincipal:
            botonseccinf["int"+str(campo)].configure(image=sabic)
        else:
            botonseccinf["int"+str(campo)].configure(image=si1e0)
    else:
        if campo%2==0:
            botonseccinf["int"+str(campo)].configure(image=sabi)
        else:
            botonseccinf["int"+str(campo)].configure(image=sabp)
    text.insert(END,"\n L"+str(campo)+"5 estado "+ str(prueba.si["SI"+str(campo)]))
    
def estadoBarraPrincipal():
    
    if prueba.barraPrincipal:
        barraPrincipal.configure(bg="green")
        for c in range(prueba.campos):
            adybt["int"+str(c+1)].configure(bg="green")
            if prueba.vs["VI"+str(c+1)]==False and prueba.i["I"+str(c+1)]==False:
                botonVeri["int"+str(c+1)].configure(bg="yellow")
            if prueba.si["SI"+str(c+1)]:
                botonseccinf["int"+str(c+1)].configure(image=sabic)
    else:
        barraPrincipal.configure(bg="black")
        for c in range(prueba.campos):
            if prueba.si["SI"+str(c+1)]:
                botonseccinf["int"+str(c+1)].configure(image=si1e0)
            else:
                if c+1%2==0:
                    botonseccinf["int"+str(c+1)].configure(image=sabi)
                else:
                    botonseccinf["int"+str(c+1)].configure(image=sabp)
            adybt["int"+str(c+1)].configure(bg="black")
            if prueba.vs["VI"+str(c+1)]==False:
                botonVeri["int"+str(c+1)].configure(bg="black")
                
def verificarSincronismo(campo):
    messagebox.showinfo(message=prueba.verificarSincronismo(campo), title="Estado")
    if prueba.vs["VI"+str(campo)]:
        botonInterruptor["int"+str(campo)].configure(image=ver)
        botonVeri["int"+str(campo)].configure(bg="green")
    text.insert(END,"\n L"+str(campo)+"0 veri Sincro "+ str(prueba.vs["VI"+str(campo)]))
    
raiz.mainloop()