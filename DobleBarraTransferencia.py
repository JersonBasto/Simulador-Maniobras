# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 15:20:43 2022

@author: j_dbg
"""

class DobleBarraTransferencia:
    def __init__(self,campos):
        self.ss={}
        self.sbp={}
        self.sbr={}
        self.i={}
        self.vs={}
        self.st={}
        self.et={}
        self.ssAcople=False
        self.siAcople=False
        self.iAcople=False
        self.barraPrincipal=False
        self.barraReserva=False
        self.campos=campos
        for campos in range(self.campos):
            self.ss["SS"+str(campos+1)]=False
            self.sbp["SBP"+str(campos+1)]=False
            self.sbr["SBR"+str(campos+1)]=False
            self.vs["VS"+str(campos+1)]=False
            self.i["I"+str(campos+1)]=False
            self.et["ET"+str(campos+1)]=True
            self.st["ST"+str(campos+1)]=False
    def estadoBarraPrincipal(self):
        mensaje=""
        contador=0
        for x in range(self.campos):
            if self.et["ET"+str(x+1)]:
                if self.sbp["SBP"+str(x+1)]:
                    if self.i["I"+str(x+1)]:
                        contador += 1
        if self.barraReserva:
            if self.iAcople:
                self.barraPrincipal=True
                mensaje="La barra principal se encuentra en "+str(self.barraPrincipal)
                print(mensaje)
            else:
                self.barraPrincipal=False
                mensaje="La barra principal se encuentra en "+str(self.barraPrincipal)
                print(mensaje)
        if contador>=1:
            self.barraPrincipal=True
            mensaje="La barra principal se encuentra en "+str(self.barraPrincipal)
            print(mensaje)
        else:
            self.barraPrincipal=False
            mensaje="La barra principal se encuentra en "+str(self.barraPrincipal)
            print(mensaje)
    def estadoBarraReserva(self):
        mensaje=""
        contador1=0
        contador2=0
        for x in range(self.campos):
            if self.et["ET"+str(x+1)]:
                if self.sbr["SBR"+str(x+1)]:
                    if self.i["I"+str(x+1)]:
                        contador1 += 1
        for x in range(self.campos):
            if self.et["ET"+str(x+1)]:
                if self.st["ST"+str(x+1)]:
                    contador2 += 1
        if contador1>=1 or contador2>=1:
            self.barraReserva=True
            mensaje="La barra reserva se encuentra en "+str(self.barraReserva)
            print(mensaje)
        elif self.barraPrincipal:
            if self.iAcople:
                self.barraReserva=True
                mensaje="La barra reserva se encuentra en "+str(self.barraReserva)
                print(mensaje)
        else:
            self.barraReserva=False
            mensaje="La barra reserva se encuentra en "+str(self.barraReserva)
            print(mensaje)
    def accionInterruptor(self,campo):
        if self.i["I"+str(campo)]==False:
            if self.ss["SS"+str(campo)]:
                if self.barraPrincipal:
                    if self.sbp["SBP"+str(campo)]:
                        if self.vs["VS"+str(campo)]:
                            self.i["I"+str(campo)]=True
                            mensaje="El interruptor "+str(campo)+" esta en estado "+str(self.i["I"+str(campo)])
                            self.estadoBarraPrincipal()
                            print(mensaje)
                        else:
                            mensaje="Debe verificar sincronismo en el interruptor "+str(campo)
                            self.estadoBarraPrincipal()
                            print(mensaje)
                else:
                    if self.sbp["SBP"+str(campo)]:
                        self.i["I"+str(campo)]=True
                        mensaje="El interruptor "+str(campo)+" esta en estado "+str(self.i["I"+str(campo)])
                        self.estadoBarraPrincipal()
                        print(mensaje)
                if self.barraReserva:
                    if self.sbr["SBR"+str(campo)]:
                        if self.vs["VS"+str(campo)]:
                            self.i["I"+str(campo)]=True
                            mensaje="El interruptor "+str(campo)+" esta en estado "+str(self.i["I"+str(campo)])
                            self.estadoBarraReserva()
                            print(mensaje)
                        else:
                            mensaje="Debe verificar sincronismo en el interruptor "+str(campo)
                            self.estadoBarraReserva()
                            print(mensaje)
                else:
                    if self.sbr["SBR"+str(campo)]:
                        self.i["I"+str(campo)]=True
                        mensaje="El interruptor "+str(campo)+" esta en estado "+str(self.i["I"+str(campo)])
                        self.estadoBarraReserva()
                        print(mensaje)
                if self.st["ST"+str(campo)]:
                    if self.iAcople:
                        if self.sbr["SBR"+str(campo)]:
                            self.i["I"+str(campo)]=True
                            mensaje="El interruptor "+str(campo)+" esta en estado "+str(self.i["I"+str(campo)])
                            self.estadoBarraReserva()()
                            print(mensaje)
                if self.i["I"+str(campo)]==False:
                    mensaje="Debe cerrar los selectores de barra del interruptor "+str(campo)
                    print(mensaje)
            else:
                mensaje="Debe cerrar el Seccionador adyacente al interruptor "+str(campo)
                print(mensaje)
        else:
            self.i["I"+str(campo)]=False
            self.vs["VS"+str(campo)]=False
            mensaje="El interruptor "+str(campo)+" esta en estado "+str(self.i["I"+str(campo)])
            self.estadoBarraPrincipal()
            self.estadoBarraReserva()
    def accionSecSuperior(self,campo):
        mensaje=""
        if self.ss["SS"+str(campo)]:
            if self.i["I"+str(campo)]:
                mensaje="No se puede abrir el seccionador ya que el Interruptor esta cerrado"
                print(mensaje)
            else:
                self.ss["SS"+str(campo)]=False
                mensaje="Estado del seccionador "+str(self.ss["SS"+str(campo)])
                print(mensaje)
        else:
            self.ss["SS"+str(campo)]=True
            mensaje="Estado del seccionador "+str(self.ss["SS"+str(campo)])
            print(mensaje)
    def accionSecBP(self,campo):
        if self.sbp["SBP"+str(campo)]==False:
            if self.i["I"+str(campo)]==True:
                if self.barraPrincipal==True:
                    if self.iAcople==True:
                        self.sbp["SBP"+str(campo)]=True
                        self.estadoBarraPrincipal()
                        self.estadoBarraReserva()
                        print(f'El estado del seccionador SBP esta en {self.sbp["SBP"+str(campo)]}')
                    else:
                        print('No puede cerrar por diferencia de potencial')
                else:
                    self.sbp["SBP"+str(campo)]=True
                    self.estadoBarraPrincipal()
                    self.estadoBarraReserva()
                    print(f'El estado del seccionador SBP esta en {self.sbp["SBP"+str(campo)]}')
            else:
                self.sbp["SBP"+str(campo)]=True
                self.estadoBarraPrincipal()
                self.estadoBarraReserva()
                print(f'El estado del seccionador SBP esta en {self.sbp["SBP"+str(campo)]}')
        else:
            contador=0
            if self.i["I"+str(campo)]==True:
                if self.sbr["SBR"+str(campo)]==True:
                    if self.barraPrincipal==True:
                        if self.iAcople==True:
                            self.sbp["SBP"+str(campo)]=False
                            self.estadoBarraPrincipal()
                            self.estadoBarraReserva()
                            print(f'El estado del seccionador SBP esta en {self.sbp["SBP"+str(campo)]}')
                        else:
                            contador=0
                            for x in range(self.campos):
                                if x+1==campo:
                                    if self.i["I"+str(x+1)]==self.i["I"+str(campo)]:
                                        pass
                                else:
                                    if self.i["I"+str(x+1)]==True and self.sbp["SBP"+str(x+1)]==True:
                                        contador=contador+1
                            if contador>=1:
                                print('No se puede accionar el Seccionador por diferencia de potencial')
                            else:
                                self.sbp["SBP"+str(campo)]=False
                                self.estadoBarraPrincipal()
                                self.estadoBarraReserva()
                                print(f'El estado del seccionador SBP esta en {self.sbp["SBP"+str(campo)]}')
                    else:
                        self.sbp["SBP"+str(campo)]=False
                        self.estadoBarraPrincipal()
                        self.estadoBarraReserva()
                        print(f'El estado del seccionador SBP esta en {self.sbp["SBP"+str(campo)]}')
                else:
                    print(f'No se puede accionar el Seccionador el interruptor {campo} esta en {self.i["I"+str(campo)]}')
            else:
                self.sbp["SBP"+str(campo)]=False
                self.estadoBarraPrincipal()
                self.estadoBarraReserva()
                print(f'El estado del seccionador SBP esta en {self.sbp["SBP"+str(campo)]}')
    def accionSecBR(self,campo):
        if self.sbr["SBR"+str(campo)]==False:
            if self.i["I"+str(campo)]==True:
                if self.barraReserva==True:
                    if self.iAcople==True:
                        self.sbr["SBR"+str(campo)]=True
                        self.estadoBarraPrincipal()
                        self.estadoBarraReserva()
                        print(f'El estado del seccionador SBR esta en {self.sbr["SBR"+str(campo)]}')
                    else:
                        print('No puede cerrar por diferencia de potencial')
                else:
                    self.sbr["SBR"+str(campo)]=True
                    self.estadoBarraPrincipal()
                    self.estadoBarraReserva()
                    print(f'El estado del seccionador SBP esta en {self.sbr["SBR"+str(campo)]}')
            else:
                self.sbr["SBR"+str(campo)]=True
                self.estadoBarraPrincipal()
                self.estadoBarraReserva()
                print(f'El estado del seccionador SBR esta en {self.sbr["SBR"+str(campo)]}')
        else:
            contador=0
            if self.i["I"+str(campo)]==True:
                if self.sbp["SBP"+str(campo)]==True:
                    if self.barraPrincipal==True:
                        if self.iAcople==True:
                            self.sbr["SBR"+str(campo)]=False
                            self.estadoBarraPrincipal()
                            self.estadoBarraReserva()
                            print(f'El estado del seccionador SBR esta en {self.sbr["SBR"+str(campo)]}')
                        else:
                            contador=0
                            for x in range(self.campos):
                                if x+1==campo:
                                    if self.i["I"+str(x+1)]==self.i["I"+str(campo)]:
                                        pass
                                else:
                                    if self.i["I"+str(x+1)]==True and self.sbr["SBR"+str(x+1)]==True:
                                        contador=contador+1
                            if contador>=1:
                                print('No se puede accionar el Seccionador por diferencia de potencial')
                            else:
                                self.sbr["SBR"+str(campo)]=False
                                self.estadoBarraPrincipal()
                                self.estadoBarraReserva()
                                print(f'El estado del seccionador SBR esta en {self.sbr["SBR"+str(campo)]}')
                    else:
                        self.sbr["SBR"+str(campo)]=False
                        self.estadoBarraPrincipal()
                        self.estadoBarraReserva()
                        print(f'El estado del seccionador SBR esta en {self.sbr["SBR"+str(campo)]}')
                else:
                    print(f'No se puede accionar el Seccionador el interruptor {campo} esta en {self.i["I"+str(campo)]}')
            else:
                self.sbr["SBR"+str(campo)]=False
                self.estadoBarraPrincipal()
                self.estadoBarraReserva()
                print(f'El estado del seccionador SBR esta en {self.sbr["SBR"+str(campo)]}')
    def accionSecST(self,campo):
        contador=0
        if self.st["ST"+str(campo)]==False:
            if True in self.st.values():
                if self.barraPrincipal==False and self.iAcople==False:
                    for x in range(self.campos):
                        if self.st["ST"+str(x+1)]==True:
                            contador= contador+1
                    if contador<=1:
                        self.st["ST"+str(campo)]=True
                        self.estadoBarraPrincipal()
                        self.estadoBarraReserva()
                        print(f'El estado del seccionador de transferencia es {self.st["ST"+str(campo)]}')
                    else:
                        print("Solamente se puede usar en el puente de paso")
                else:
                    print("La barra solo puede soportar un campo de linea")
            else:
                if self.iAcople==True:
                    if self.i["I"+str(campo)]==False:
                        if self.barraReserva==True and self.et["ET"+str(campo)]==True:
                            print("No se puede cerrar el seccionador ya que hay diferencia de potencial")
                        else:
                            self.st["ST"+str(campo)]=True
                            self.estadoBarraPrincipal()
                            self.estadoBarraReserva()
                            print(f'El estado del seccionador de transferencia es {self.st["ST"+str(campo)]}')
                            print("Se transfirieron las protecciones")
                    else:
                        self.st["ST"+str(campo)]=True
                        self.estadoBarraPrincipal()
                        self.estadoBarraReserva()
                        print(f'El estado del seccionador de transferencia es {self.st["ST"+str(campo)]}')
                        print("Se transfirieron las protecciones")
                else:
                    if self.barraPrincipal==True:
                        print("Debe cerrar el interruptor de acople para transferir protecciones")
                    elif self.barraReserva==True:
                        self.st["ST"+str(campo)]=True
                        self.estadoBarraPrincipal()
                        self.estadoBarraReserva()
                        print(f'El estado del seccionador de transferencia es {self.st["ST"+str(campo)]}')
                    else:
                        self.st["ST"+str(campo)]=True
                        self.estadoBarraPrincipal()
                        self.estadoBarraReserva()
                        print(f'El estado del seccionador de transferencia es {self.st["ST"+str(campo)]}')
                        print('Inicio de puente de paso')
        else:
            if self.i["I"+str(campo)]==True:
                self.st["ST"+str(campo)]=False
                self.estadoBarraPrincipal()
                self.estadoBarraReserva()
                print(f'El estado del seccionador de transferencia es {self.st["ST"+str(campo)]}')
            else:
                if self.et["ET"+str(campo)]==True:
                    if self.iAcople==True and self.barraPrincipal==True:
                        if True in self.i.values():
                            print("No se puede realizar la operacion entraria en diferencia de potencial")
                        else:
                            self.st["ST"+str(campo)]=False
                            self.estadoBarraPrincipal()
                            self.estadoBarraReserva()
                            print(f'El estado del seccionador de transferencia es {self.st["ST"+str(campo)]}')     
                    else:
                        self.st["ST"+str(campo)]=False
                        self.estadoBarraPrincipal()
                        self.estadoBarraReserva()
                        print(f'El estado del seccionador de transferencia es {self.st["ST"+str(campo)]}')
                else:
                    self.st["ST"+str(campo)]=False
                    self.estadoBarraPrincipal()
                    self.estadoBarraReserva()
                    print(f'El estado del seccionador de transferencia es {self.st["ST"+str(campo)]}')
            
        
                