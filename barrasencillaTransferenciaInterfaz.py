# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 14:22:57 2022

@author: j_dbg
"""

from BarraSencillaTransferencia import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo
import PIL.Image
import PIL.ImageTk

botonET={}
adyet={}
botonseccsup={}
botonInterruptor={}
botonseccinf={}
adybp={}
botonVeri={}

adyetst={}
botonsecctrans={}
adybt={}


label={}
botonError={}

raiz=Tk()
raiz.title("Simulador Barra Sencilla")
capap=Frame(raiz,bg="#F1ECEB",width=600,height=500)
capa1=Frame(capap,bg="#FFFF00",width=200, height=200,relief="sunken",borderwidth=3)
capa2=Frame(capap,bg="black",width=400, height=400,relief="sunken",borderwidth=3)
capa3=Frame(capap,bg="#000F00",width=200, height=200)
capa4=Frame(capap,bg="black",width=200, height=200,relief="sunken",borderwidth=3)
canvas2=Canvas(capa2,bg='white')
canvas3=Canvas(capa4,bg="white")
canvas4=Canvas(capa3,bg="white",width=200, height=200,relief="sunken",borderwidth=3)
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
prueba=BarraSencillaTransferencia(campos)
altura=0
ancho=0
if prueba.campos%2==0:
    ancho=prueba.campos/2
else:
    ancho=(prueba.campos+1)/2
Frame1=Frame(canvas2,bg='white', width=(250*ancho)+40, height=800)
Frame3=Frame(canvas4,bg="white",width=100, height=20*prueba.campos)

####Se expande con Grid la ventana raiz o root
raiz.rowconfigure(0, weight=1)
raiz.columnconfigure(0, weight=1)
###Se aplica la propiedad de expandirse a la capa1 
capap.grid(sticky=NSEW)
capap.grid_columnconfigure(1, weight=1)
capap.grid_rowconfigure(0, weight=1)
capap.grid_rowconfigure(1, weight=1)
###Se configura Scroll
scrollCapa2=Scrollbar(capa2,orient="vertical",command=canvas2.yview)
scrollxCapa2=Scrollbar(capa2, orient="horizontal",command=canvas2.xview)
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
###----------------------------------------------------------------------------------------
scrollCapa3=Scrollbar(capa3,orient="vertical",command=canvas4.yview)
scrollxCapa3=Scrollbar(capa3, orient="horizontal",command=canvas4.xview)
scrollCapa3.pack(side=RIGHT,fill=Y)
scrollxCapa3.pack(side=BOTTOM,fill=X)
canvas4.configure(yscrollcommand=scrollCapa3.set, xscrollcommand=scrollxCapa3.set)
canvas4.bind('<Configure>', lambda e: canvas4.configure(scrollregion= canvas4.bbox("all")))
###------------###----------------###---------------###--------------###---------------
canvas2.pack(fill=BOTH,expand=1)
canvas3.pack(fill=BOTH,expand=1)
canvas4.pack(fill=BOTH,expand=1)
text.grid(row=0,column=0)
##Se ubica Capa 2 y capa 3
canvas2.create_window((0,0), window=Frame1, anchor='nw')
canvas4.create_window((0,0), window=Frame3, anchor='nw')
capa1.grid(row=0, rowspan=2,column=0,padx=(10,10),pady=(10,10),sticky=NSEW)
capa2.grid(row=0, rowspan=2,column=1,padx=(10,10),pady=(10,10),sticky=NSEW)
capa3.grid(row=0, column=2,padx=(10,10),pady=(10,10),sticky='EWNS')
capa4.grid(row=1, column=2,padx=(10,10),pady=(10,10),sticky='EWNS')

barraPrincipal=Label(Frame1, bg="black", bd=3, relief="ridge" )
barraPrincipal.place(x=20,y=270,width=250*ancho,height=20)
barraTransferencia=Label(Frame1, bg="black", bd=3, relief="ridge" )
barraTransferencia.place(x=20,y=460,width=250*ancho,height=20)
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
#----------------------#####FUNCIONES#####_--------------------------------
def accionInterruptor(campo):
    messagebox.showinfo(message=prueba.accionInterruptor(campo), title="Estado")
    if prueba.i["I"+str(campo)]:
        botonInterruptor["int"+str(campo)].configure(image=intece)
        botonVeri["int"+str(campo)].configure(bg="green")
    else:
        botonInterruptor["int"+str(campo)].configure(image=intea)
    text.insert(END,"\n L"+str(campo)+"0 estado "+ str(prueba.i["I"+str(campo)]))
    estadoBarraPrincipal()
    estadoBarraTransferencia()
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
def accionSecST(campo):
    messagebox.showinfo(message=prueba.accionSecTransferencia(campo), title="Estado")
    if prueba.st["ST"+str(campo)]:
        botonsecctrans["int"+str(campo)].configure(image=sabic)
    else:
        botonsecctrans["int"+str(campo)].configure(image=sabp)
    text.insert(END,"\n L"+str(campo)+"7 estado "+ str(prueba.st["ST"+str(campo)]))
    estadoBarraPrincipal()
    estadoBarraTransferencia()
def verificarSincronismo(campo):
    messagebox.showinfo(message=prueba.verificarSincronismo(campo), title="Estado")
    if prueba.vs["VS"+str(campo)]:
        botonInterruptor["int"+str(campo)].configure(image=ver)
        botonVeri["int"+str(campo)].configure(bg="green")
    text.insert(END,"\n L"+str(campo)+"0 veri Sincro "+ str(prueba.vs["VI"+str(campo)]))
def accionIntAcople():
    messagebox.showinfo(message=prueba.accionIntAcople(), title="Estado")
    if prueba.intAcople:
        iAcople.configure(image=intece)
    else:
        iAcople.configure(image=intea)
    text.insert(END,"\n O10 estado "+ str(prueba.intAcople))
    estadoBarraPrincipal()
    estadoBarraTransferencia()
def accionSecSupAcople():
    messagebox.showinfo(message=prueba.accionSecSupAcople(), title="Estado")
    if prueba.ssAcople:
        ssAcople.configure(image=sabic)
    else:
        ssAcople.configure(image=sabp)
    text.insert(END,"\n O13 estado "+ str(prueba.ssAcople))
def accionSecInfAcople():
    messagebox.showinfo(message=prueba.accionSecInfAcople(), title="Estado")
    if prueba.siAcople:
        siAcople.configure(image=si1e0)
    else:
        siAcople.configure(image=sabp)
    text.insert(END,"\n O15 estado "+ str(prueba.siAcople))
def estadoBarraPrincipal():
    if prueba.barraPrincipal:
        barraPrincipal.configure(bg="green")
        adysAcople.configure(bg="green")
        for x in range(prueba.campos):
           adybp["int"+str(x+1)].configure(bg="green")
           if prueba.vs["VS"+str(x+1)]==False and prueba.i["I"+str(x+1)]==False:
               botonVeri["int"+str(x+1)].configure(bg="yellow")
           if prueba.si["SI"+str(x+1)]:
               botonseccinf["int"+str(x+1)].configure(image=sabic)
           else:
               botonseccinf["int"+str(x+1)].configure(image=sabp)
    else:
        barraPrincipal.configure(bg="black")
        adysAcople.configure(bg="black")
        for x in range(prueba.campos):
           adybp["int"+str(x+1)].configure(bg="black")
           if prueba.vs["VS"+str(x+1)]==False and prueba.i["I"+str(x+1)]==False:
               botonVeri["int"+str(x+1)].configure(bg="black")
           if prueba.si["SI"+str(x+1)]:
               botonseccinf["int"+str(x+1)].configure(image=si1e0)
           else:
               botonseccinf["int"+str(x+1)].configure(image=sabp)
def estadoBarraTransferencia():
    if prueba.barraTransferencia:
        barraTransferencia.configure(bg="green")
        adyiAcople.configure(bg="green")
        if prueba.siAcople:
            siAcople.configure(image=sabic)
        for c in range(prueba.campos):
            adybt["int"+str(c+1)].configure(bg="green")
    else:
        barraTransferencia.configure(bg="black")
        adyiAcople.configure(bg="black")
        if prueba.siAcople:
            siAcople.configure(image=si1e0)
        for c in range(prueba.campos):
            adybt["int"+str(c+1)].configure(bg="black")
def estadoExtremoRemoto(campo):
    messagebox.showinfo(message=prueba.accionExtremo(campo), title="Estado")
    if prueba.et["ET"+str(campo)]:
        adyet["int"+str(campo)].configure(bg="green")
        adyetst["int"+str(campo)].configure(bg="green")
        botonET["int"+str(campo)].configure(bg="green")
        estadoBarraPrincipal()
        estadoBarraTransferencia()
        text.insert(END,"\n ET"+str(campo)+" estado "+ str(prueba.et["ET"+str(campo)]))
    else:
        adyet["int"+str(campo)].configure(bg="black")
        adyetst["int"+str(campo)].configure(bg="black")
        botonET["int"+str(campo)].configure(bg="white")
        estadoBarraPrincipal()
        estadoBarraTransferencia()
        text.insert(END,"\n ET"+str(campo)+" estado "+ str(prueba.et["ET"+str(campo)]))
#--------------------------------------Campo de Acople------------------------
label["IA"]=Label(Frame1, text="O10")
label["IA"].place(x=((250*ancho)/2)-10,y=350, width=50, height=50)
label["SSA"]=Label(Frame1, text="O13")
label["SSA"].place(x=((250*ancho)/2)-10,y=300, width=50, height=50)
label["SIA"]=Label(Frame1, text="O15")
label["SIA"].place(x=((250*ancho)/2)-10,y=400, width=50, height=50)
adysAcople=Label(Frame1, bg="black", bd=3, relief="ridge" )
adysAcople.place(x=((250*ancho)/2)-50+15,y=290, width=20, height=10)
iAcople=Button(Frame1,text="IA",image=intea, command=accionIntAcople)
iAcople.place(x=((250*ancho)/2)-50,y=350, width=50, height=50)
ssAcople=Button(Frame1,text="SSA",image=sabp, command=accionSecSupAcople)
ssAcople.place(x=((250*ancho)/2)-50,y=300, width=50, height=50)
siAcople=Button(Frame1,text="SSA",image=sabp, command=accionSecInfAcople)
siAcople.place(x=((250*ancho)/2)-50,y=400, width=50, height=50)
adyiAcople=Label(Frame1, bg="black", bd=3, relief="ridge" )
adyiAcople.place(x=((250*ancho)/2)-50+15,y=450, width=20, height=10)
#----------------------------Botones-------------------------------------------
for c in range(campos):
    x=c+1
    if x%2==0:
        correr=((((x)/2)-1)*250)
        botonET["int"+str(c+1)]=Button(Frame1,text="ET"+ str(c+1),command=lambda x=x : estadoExtremoRemoto(x),bg="green")
        adyet["int"+str(c+1)]=Label(Frame1, bg='green', bd=3,relief="ridge")
        adyetst["int"+str(c+1)]=Label(Frame1, bg='green', bd=3,relief="ridge")
        botonsecctrans["int"+str(c+1)]=Button(Frame1,text="SS "+ str(c+1),command=lambda x=x : accionSecST(x),image=sabp)
        botonseccsup["int"+str(c+1)]=Button(Frame1,text="SS "+ str(c+1),command=lambda x=x : accionSecSuperior(x),image=sabp)
        botonInterruptor["int"+str(c+1)]=Button(Frame1,text="I "+ str(c+1), command=lambda x=x : accionInterruptor(x),image=intea)
        botonVeri["int"+str(c+1)]=Button(Frame1,bg="black",command=lambda x=x : verificarSincronismo(x))
        botonseccinf["int"+str(c+1)]=Button(Frame1,text="SI"+ str(c+1),command=lambda x=x : accionSecInferior(x),image=sabp)
        adybt["int"+str(c+1)]=Label(Frame1, bg='black', bd=3,relief="ridge")
        adybp["int"+str(c+1)]=Label(Frame1, bg='black', bd=3,relief="ridge")
        #----------------Labels--------------------------------------
        label["SS"+str(c+1)]=Label(Frame1,bg="white", text="L"+str(c+1)+"3")
        label["ST"+str(c+1)]=Label(Frame1,bg="white", text="L"+str(c+1)+"7")
        label["I"+str(c+1)]=Label(Frame1,bg="white", text="L"+str(c+1)+"0")
        label["VS"+str(c+1)]=Label(Frame1,bg="white", text="Ver L"+str(c+1)+"0")
        label["SI"+str(c+1)]=Label(Frame1,bg="white", text="L"+str(c+1)+"5")
        #----------------Posicion Botones-------------------------------------
        botonET["int"+str(c+1)].place(x=40+correr,y=700,width=50 ,height=50)
        adyet["int"+str(c+1)].place(x=55+correr,y=650,width=20 ,height=50)
        adyetst["int"+str(c+1)].place(x=75+correr,y=665,width=100, height=20)
        botonsecctrans["int"+str(c+1)].place(x=140+correr,y=615,width=50 ,height=50)
        botonseccsup["int"+str(c+1)].place(x=40+correr, y=600,width=50,height=50)
        botonInterruptor["int"+str(c+1)].place(x=40+correr,y=550,width=50,height=50)
        botonVeri["int"+str(c+1)].place(x=90+correr,y=550,width=10,height=50)
        botonseccinf["int"+str(c+1)].place(x=40+correr,y=500,width=50,height=50)
        adybt["int"+str(c+1)].place(x=155+correr,y=480,width=20 ,height=135)
        adybp["int"+str(c+1)].place(x=55+correr,y=290,width=20,height=210)
        #----------------Posicion Labels-------------------------------------
        label["SS"+str(c+1)].place(x=90+correr, y=600,width=50,height=50)
        label["ST"+str(c+1)].place(x=190+correr,y=615,width=50 ,height=50)
        label["I"+str(c+1)].place(x=100+correr,y=575,width=40,height=25)
        label["VS"+str(c+1)].place(x=100+correr,y=550,width=40,height=25)
        label["SI"+str(c+1)].place(x=90+correr,y=500,width=50,height=50)
    else:
        correr=((((x+1)/2)-1)*250)
        botonET["int"+str(c+1)]=Button(Frame1,text="ET"+ str(c+1),command=lambda x=x : estadoExtremoRemoto(x),bg="green")
        adyet["int"+str(c+1)]=Label(Frame1, bg='green', bd=3,relief="ridge")
        adyetst["int"+str(c+1)]=Label(Frame1, bg='green', bd=3,relief="ridge")
        botonsecctrans["int"+str(c+1)]=Button(Frame1,text="SS "+ str(c+1),command=lambda x=x : accionSecST(x),image=sabp)
        botonseccsup["int"+str(c+1)]=Button(Frame1,text="SS "+ str(c+1),command=lambda x=x : accionSecSuperior(x),image=sabp)
        botonInterruptor["int"+str(c+1)]=Button(Frame1,text="I "+ str(c+1), command=lambda x=x : accionInterruptor(x),image=intea)
        botonVeri["int"+str(c+1)]=Button(Frame1,bg="black",command=lambda x=x : verificarSincronismo(x))
        botonseccinf["int"+str(c+1)]=Button(Frame1,text="SI"+ str(c+1),command=lambda x=x : accionSecInferior(x),image=sabp)
        adybt["int"+str(c+1)]=Label(Frame1, bg='black', bd=3,relief="ridge")
        adybp["int"+str(c+1)]=Label(Frame1, bg='black', bd=3,relief="ridge")
        #----------------Labels--------------------------------------
        label["SS"+str(c+1)]=Label(Frame1,bg="white", text="L"+str(c+1)+"3")
        label["ST"+str(c+1)]=Label(Frame1,bg="white", text="L"+str(c+1)+"7")
        label["I"+str(c+1)]=Label(Frame1,bg="white", text="L"+str(c+1)+"0")
        label["VS"+str(c+1)]=Label(Frame1,bg="white", text="Ver L"+str(c+1)+"0")
        label["SI"+str(c+1)]=Label(Frame1,bg="white", text="L"+str(c+1)+"5")
        #----------------Posicion Botones-------------------------------------
        botonET["int"+str(c+1)].place(x=40+correr,y=0,width=50 ,height=50)
        adyet["int"+str(c+1)].place(x=55+correr,y=50,width=20 ,height=50)
        adyetst["int"+str(c+1)].place(x=75+correr,y=65,width=100, height=20)
        botonsecctrans["int"+str(c+1)].place(x=140+correr,y=85,width=50 ,height=50)
        botonseccsup["int"+str(c+1)].place(x=40+correr, y=100,width=50,height=50)
        botonInterruptor["int"+str(c+1)].place(x=40+correr,y=150,width=50,height=50)
        botonVeri["int"+str(c+1)].place(x=90+correr,y=150,width=10,height=50)
        botonseccinf["int"+str(c+1)].place(x=40+correr,y=200,width=50,height=50)
        adybt["int"+str(c+1)].place(x=155+correr,y=135,width=20 ,height=325)
        adybp["int"+str(c+1)].place(x=55+correr,y=250,width=20,height=20)
        #----------------Posicion Labels-------------------------------------
        label["SS"+str(c+1)].place(x=90+correr, y=100,width=50,height=50)
        label["ST"+str(c+1)].place(x=190+correr,y=85,width=50 ,height=50)
        label["I"+str(c+1)].place(x=100+correr,y=150,width=40,height=25)
        label["VS"+str(c+1)].place(x=100+correr,y=175,width=40,height=25)
        label["SI"+str(c+1)].place(x=90+correr,y=200,width=50,height=50)
#---------------------------------Funciones Errores----------------------------------------
def fallaInterruptor(event):
    campo=lista.get()
    messagebox.showinfo(message="Se realizara Falla en el interruptor "+str(campo), title="Falla Interruptor")
    if prueba.i["I"+str(campo)]:
        accionInterruptor(campo)
    else:
        prueba.i["I"+str(campo)]=True
        accionInterruptor(campo)
    botonInterruptor["int"+str(campo)].configure(image=intea, state=DISABLED)
    lista.configure(state=DISABLED)
    lista2.configure(state=DISABLED)
    botonEvaluar.configure(state=ACTIVE)
def mantoInterruptor(event):
    campo=lista2.get()
    messagebox.showinfo(message="Se realizara Manto en el interruptor "+str(campo), title="Manto Interruptor")
    lista.configure(state=DISABLED)
    lista2.configure(state=DISABLED)
    botonEvaluar2.configure(state=ACTIVE)
#---------------------------------Comprobantes----------------------------------------
def comprobarFalla():
    campo=lista.get()
    if prueba.et["ET"+str(campo)]:
        if prueba.st["ST"+str(campo)]:
            if prueba.intAcople:
                messagebox.showinfo(message="Reestablecimiento realizado", title="Exito")
                lista.configure(state=ACTIVE)
                lista2.configure(state=ACTIVE)
                botonEvaluar.configure(state=DISABLED)
                botonInterruptor["int"+str(campo)].configure(state=ACTIVE)
            else:
                messagebox.showinfo(message="Interruptor de Acople Abierto", title="Error")
        else:
            messagebox.showinfo(message="Seccionador de Transferencia Abierto", title="Error")
    else:
        messagebox.showinfo(message="Extremo Remoto Abierto", title="Error")
def comprobarManto():
    campo=lista2.get()
    if prueba.i["I"+str(campo)]==False:
        if prueba.et["ET"+str(campo)]:
            if prueba.st["ST"+str(campo)]:
                if prueba.intAcople:
                    messagebox.showinfo(message="Reestablecimiento realizado", title="Exito")
                    lista.configure(state=ACTIVE)
                    lista2.configure(state=ACTIVE)
                    botonEvaluar2.configure(state=DISABLED)
                    botonInterruptor["int"+str(campo)].configure(state=ACTIVE)
                else:
                    messagebox.showinfo(message="Interruptor de Acople Abierto", title="Error")
            else:
                messagebox.showinfo(message="Seccionador de Transferencia Abierto", title="Error")
        else:
            messagebox.showinfo(message="Extremo Remoto Abierto", title="Error")
    else:
        messagebox.showinfo(message="El Interruptor sigue cerrado", title="Error")
#---------------------------------Botones Errores----------------------------------------
lista=ttk.Combobox(Frame3, state="readondly")
valores=[0]*prueba.campos
label["FI"]=Label(Frame3, text="Falla en el interruptor :", bg="white",)
label["FI"].grid(row=0,column=0,pady=5)
for c in range(prueba.campos):
    valores[c]=str(c+1)
lista["values"]=valores
lista.grid(row=1,column=0,pady=5)
lista.bind("<<ComboboxSelected>>",fallaInterruptor)
botonEvaluar=Button(Frame3,text="Evaluar",state=DISABLED,command=comprobarFalla)
botonEvaluar.grid(row=2,column=0,padx=10,pady=5)
#---------------------------------Botones Mantenimiento----------------------------------------
lista2=ttk.Combobox(Frame3, state="readondly")
valores2=[0]*prueba.campos
label["FM"]=Label(Frame3, text="Mantenimineto en el interruptor :", bg="white")
label["FM"].grid(row=3,column=0,pady=5)
for c in range(prueba.campos):
    valores2[c]=str(c+1)
lista2["values"]=valores2
lista2.grid(row=4,column=0,pady=5)
lista2.bind("<<ComboboxSelected>>",mantoInterruptor)
botonEvaluar2=Button(Frame3,text="Evaluar",state=DISABLED,command=comprobarManto)
botonEvaluar2.grid(row=5,column=0,pady=5)

raiz.mainloop()

