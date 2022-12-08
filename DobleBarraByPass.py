# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 11:02:22 2022

@author: j_dbg
"""

class dobleBarraByPass:
    def __init__(self,campos):
        self.campos=campos
        self.i={}
        self.ss={}
        self.si={}
        self.sbp={}
        self.sbr={}
        self.sbpass={}
        self.et={}
        self.vs={}
        self.ssAcople=False
        self.siAcople=False
        self.iAcople=False
        self.barraPrincipal=False
        self.barraReserva=False
        self.vsAcople=False
        for campos in range(self.campos):
            self.i["I"+str(campos+1)]=False
            self.ss["SS"+str(campos+1)]=False
            self.si["SS"+str(campos+1)]=False
            self.sbp["SBP"+str(campos+1)]=False
            self.sbr["SBR"+str(campos+1)]=False
            self.sbpass["SBPASS"+str(campos+1)]=False
            self.et["ET"+str(campos+1)]=True
            self.vs["VS"+str(campos+1)]=False
    def estadoBarraPrincipal(self):
        mensaje=""
        contador1=0
        contador2=0
        for x in range(self.campos):
            if self.et["ET"+str(x+1)]:
                if self.sbp["SBP"+str(x+1)]:
                    if self.i["I"+str(x+1)]:
                        contador1 += 1
        for x in range(self.campos):
            if self.et["ET"+str(x+1)]:
                if self.sbpass["SBPASS"+str(x+1)]:
                    if self.sbp["SBP"+str(x+1)]:
                        contador2 += 1
        if self.barraReserva:
            if self.iAcople:
                self.barraPrincipal=True
                mensaje="La barra principal se encuentra en "+str(self.barraPrincipal)
                print(mensaje)
            else:
                self.barraPrincipal=False
                mensaje="La barra principal se encuentra en "+str(self.barraPrincipal)
                print(mensaje)
        if contador1>=1 or contador2>=1:
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
                if self.sbpass["SBPASS"+str(x+1)]:
                    if self.sbr["SBR"+str(x+1)]:
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
            if self.ss["SS"+str(campo)] and self.si["SI"+str(campo)]:
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
                if self.sbpass["SBPASS"+str(campo)]:
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
                mensaje="Debe cerrar los Seccionadores adyacentes al interruptor "+str(campo)
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
    def accionSecInferior(self,campo):
        if self.si["SI"+str(campo)]==False:
            self.si["SI"+str(campo)]=True
            print(f'El seccionador superior de {campo} esta en {self.si["SI"+str(campo)]}')
            mensaje="El seccionador superior de "+str(campo)+" esta en" +str(self.si["SI"+str(campo)])
        else:
            if self.i["I"+str(campo)]==False:
                self.si["SI"+str(campo)]=False
                print(f'El seccionador superior de {campo} esta en {self.si["SI"+str(campo)]}')
                mensaje="El seccionador superior de "+str(campo)+" esta en " +str(self.si["SI"+str(campo)])
            else:
                print(f'No se puede abrir el seccionador ya que el interruptor esta en {self.i["I"+str(campo)]}')
                mensaje="No se puede abrir el seccionador ya que el interruptor esta en "+str(self.i["I"+str(campo)])
        return mensaje
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
    def accionSecBPass(self,campo):
        contador=0
        if self.sbpass["SBPASS"+str(campo)]==False:
            if True in self.sbpass.values():
                if self.barraPrincipal==False and self.iAcople==False:
                    for x in range(self.campos):
                        if self.sbpass["SBPASS"+str(x+1)]==True:
                            contador= contador+1
                    if contador<=1:
                        self.sbpass["SBPASS"+str(campo)]=True
                        self.estadoBarraPrincipal()
                        self.estadoBarraReserva()
                        print(f'El estado del seccionador de transferencia es {self.sbpass["SBPASS"+str(campo)]}')
                    else:
                        print("Solamente se puede usar en el puente de paso")
                else:
                    print("La barra solo puede soportar un campo de linea")
            else:
                alone=False
                contadorBP=0
                contadorBR=0
                for x in range(self.campos):
                    if self.sbp["SBP"+str(x+1)]:
                        contadorBP +=1
                    if self.sbr["SBR"+str(x+1)]:
                        contadorBR +=1
                    if x+1==campo:
                        if self.sbp["SBP"+str(x+1)]:
                            contadorBP -=1
                        if self.sbr["SBR"+str(x+1)]:
                            contadorBR -=1
                print("Contador BP ",contadorBP)
                print("Contador BR ",contadorBR)
                if contadorBP==0:
                    alone=True
                if contadorBR==0:
                    alone=True
                if self.iAcople==True:
                    if self.i["I"+str(campo)]==False:
                        if self.et["ET"+str(campo)]==True:
                            if self.sbp["SBP"+str(campo)] or self.sbr["SBR"+str(campo)]:
                                print("No se puede cerrar el seccionador ya que hay diferencia de potencial")
                        else:
                            if alone:
                                self.sbpass["SBPASS"+str(campo)]=True
                                self.estadoBarraPrincipal()
                                self.estadoBarraReserva()
                                print(f'El estado del seccionador de transferencia es {self.sbpass["SBPASS"+str(campo)]}')
                                print("Se transfirieron las protecciones")
                            else:
                                if contadorBP>contadorBR:
                                    print("Mueva los demas campos de linea a la Barra Principal menos el campo de linea {campo}")
                                elif contadorBR>contadorBP:
                                    print("Mueva los demas campos de linea a la Barra Reserva menos el campo de linea {campo}")
                    else:
                        if alone:
                            self.sbpass["SBPASS"+str(campo)]=True
                            self.estadoBarraPrincipal()
                            self.estadoBarraReserva()
                            print(f'El estado del seccionador de transferencia es {self.sbpass["SBPASS"+str(campo)]}')
                            print("Se transfirieron las protecciones")
                        else:
                            if contadorBP>contadorBR:
                                print(f'Mueva los demas campos de linea a la Barra Principal menos el campo de linea {campo}')
                            elif contadorBR>contadorBP:
                                print(f'Mueva los demas campos de linea a la Barra Reserva menos el campo de linea {campo}')
                else:
                    if self.barraPrincipal==True:
                        contadorBP=0
                        for campo in range(self.campos):
                            if self.i["I"+str(campo+1)]:
                                if self.sbp["SBP"+str(campo+1)]:
                                    contadorBP +=1
                        if contadorBP>=1:
                            print("Debe cerrar es interruptor de acople para transferir protecciones")
                            mensaje="Debe cerrar es interruptor de acople para transferir protecciones"
                        else:
                            self.sbpass["SBPASS"+str(campo)]=True
                            self.estadoBarraPrincipal()
                            self.estadoBarraReserva()
                            print(f'El estado del seccionador de transferencia es {self.sbpass["SBPASS"+str(campo)]}')
                    elif self.barraReserva==True:
                        contadorBP=0
                        for campo in range(self.campos):
                            if self.i["I"+str(campo+1)]:
                                if self.sbr["SBR"+str(campo+1)]:
                                    contadorBP +=1
                        if contadorBP>=1:
                            print("Debe cerrar es interruptor de acople para transferir protecciones")
                            mensaje="Debe cerrar es interruptor de acople para transferir protecciones"
                        else:
                            self.sbpass["SBPASS"+str(campo)]=True
                            self.estadoBarraPrincipal()
                            self.estadoBarraReserva()
                            print(f'El estado del seccionador de transferencia es {self.sbpass["SBPASS"+str(campo)]}')
                    else:
                        self.sbpass["SBPASS"+str(campo)]=True
                        self.estadoBarraPrincipal()
                        self.estadoBarraReserva()
                        print(f'El estado del seccionador de transferencia es {self.sbpass["SBPASS"+str(campo)]}')
                        print('Inicio de puente de paso')
        else:
            if self.i["I"+str(campo)]==True:
                self.sbpass["SBPASS"+str(campo)]=False
                self.estadoBarraPrincipal()
                self.estadoBarraReserva()
                print(f'El estado del seccionador de transferencia es {self.sbpass["SBPASS"+str(campo)]}')
            else:
                if self.et["ET"+str(campo)]==True:
                    if self.iAcople==True:
                        if self.barraPrincipal==True or self.barraReserva==True:
                            if True in self.i.values():
                                print("No se puede realizar la operacion entraria en diferencia de potencial")
                            else:
                                self.sbpass["SBPASS"+str(campo)]=False
                                self.estadoBarraPrincipal()
                                self.estadoBarraReserva()
                                print(f'El estado del seccionador de transferencia es {self.sbpass["SBPASS"+str(campo)]}')     
                    else:
                        self.sbpass["SBPASS"+str(campo)]=False
                        self.estadoBarraPrincipal()
                        self.estadoBarraReserva()
                        print(f'El estado del seccionador de transferencia es {self.sbpass["SBPASS"+str(campo)]}')
                else:
                    self.sbpass["SBPASS"+str(campo)]=False
                    self.estadoBarraPrincipal()
                    self.estadoBarraReserva()
                    print(f'El estado del seccionador de transferencia es {self.sbpass["SBPASS"+str(campo)]}')
    def accionVerInt(self,campo):
        contadorBP=0
        contadorBR=0
        for x in range(self.campos):
            if self.i["I"+str(x+1)]==True and self.sbp["SBP"+str(x+1)]==True:
                pass
            else:
                contadorBP= contadorBP+1
            if self.i["I"+str(x+1)]==True and self.sbr["SBR"+str(x+1)]==True:
                pass
            else:
                contadorBR= contadorBR+1
        if contadorBP>=1 or contadorBR>=1:
            self.vs["VS"+str(campo)]=True
            print("Se ha verificado Sincronismo")
        else:
            print("No es necesario verificar sincronismo")
    def accionVerIntAcople(self):
        if self.barraPrincipal==True and self.barraReserva==True:
            self.vsAcople=True
            print("Se ha verificado Sincronismo")
        else:
            print("No es necesario verificar sincronismo")
    def accionSecSupAcople(self):
        if self.ssAcople==False:
            self.ssAcople=True
            print(f'El estado del SS Acople es {self.ssAcople}')
        else:
            if self.iAcople==True:
                print("No se puede accionat ya que el int Acople esta en {self.iAcople}")
            else:
                self.ssAcople=False
                print(f'El estado del SS Acople es {self.ssAcople}')
    def accionSecInfAcople(self):
        if self.siAcople==False:
            self.siAcople=True
            print(f'El estado del SI Acople es {self.siAcople}')
        else:
            if self.iAcople==True:
                print("No se puede accionat ya que el int Acople esta en {self.iAcople}")
            else:
                self.siAcople=False
                print(f'El estado del SI Acople es {self.siAcople}')
    def accionIntAcople(self):
        if self.iAcople==False:
            if self.ssAcople==False or self.siAcople==False:
                print("Debe cerrar los seccionadores adyacentes")
            else:
                if self.barraPrincipal==True and self.barraReserva==True:
                    if self.vsAcople==False:
                        print("Debe verificar sincronismo")
                    else:
                        self.iAcople=True
                        self.estadoBarraPrincipal()
                        self.estadoBarraReserva()
                        print(f'El interruptor de acople esta en {self.iAcople}')
                else:
                    self.iAcople=True
                    self.estadoBarraPrincipal()
                    self.estadoBarraReserva()
                    print(f'El interruptor de acople esta en {self.iAcople}')
        else:
            self.iAcople=False
            self.vsAcople=False
            self.estadoBarraPrincipal()
            self.estadoBarraReserva()
            print(f'El interruptor de acople esta en {self.iAcople}')
prueba=dobleBarraByPass(4)
prueba.accionSecSuperior(1)
prueba.accionSecSuperior(2)
prueba.accionSecSuperior(3)
prueba.accionSecSuperior(4)
prueba.accionSecBP(1)
prueba.accionSecBP(2)
prueba.accionSecBR(3)
prueba.accionSecBR(4)
prueba.accionInterruptor(1)
prueba.accionVerInt(2)
prueba.accionInterruptor(2)
prueba.accionInterruptor(3)           
prueba.accionVerInt(4)
prueba.accionInterruptor(4)
prueba.accionSecSupAcople()
prueba.accionSecInfAcople()
prueba.accionVerIntAcople()
prueba.accionIntAcople()
print("Interruptor 1 en ",prueba.i["I1"])
print("Interruptor 2 en ",prueba.i["I2"] )
print("Interruptor 3 en ",prueba.i["I3"] )
print("Interruptor 4 en ",prueba.i["I4"] )
print("Interruptor de acople en ",prueba.iAcople)
print("Barra Principal esta en ",prueba.barraPrincipal)
print("Barra Reserva esta en ",prueba.barraReserva)
            