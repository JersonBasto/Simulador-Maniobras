# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 09:59:32 2022

@author: j_dbg
"""

class dobleBarra:
    def __init__(self,campos):
        self.campos=campos
        self.ss={}
        self.sbp={}
        self.sbr={}
        self.vs={}
        self.i={}
        self.barraPrincipal=False
        self.barraReserva=False
        self.intAcople=False
        self.ssAcople=False
        self.siAcople=False
        self.vsAcople=False
        for campo in range(campos):
            self.ss["SS"+str(campo+1)]=False
            self.sbp["SBP"+str(campo+1)]=False
            self.sbr["SBR"+str(campo+1)]=False
            self.vs["VS"+str(campo+1)]=False
            self.i["I"+str(campo+1)]=False
    def estadoBarraPrincipal(self):#########Mejorar BArras##########
        contador=0
        for campo in range(self.campos):
            if self.i["I"+str(campo+1)]==True and self.sbp["SBP"+str(campo+1)]==True:
                contador = contador +1
        if contador>=1:
            self.barraPrincipal=True
            print(f'La barra principal esta en {self.barraPrincipal}')
            mensaje="La barra principal esta en "+str(self.barraPrincipal)
        else:
            if self.barraReserva==True and self.intAcople==True:
                self.barraPrincipal=True
                print(f'La barra principal esta en {self.barraPrincipal}')
                mensaje="La barra principal esta en "+str(self.barraPrincipal)
            else:
                self.barraPrincipal=False
                print(f'La barra principal esta en {self.barraPrincipal}')
                mensaje="La barra principal esta en "+str(self.barraPrincipal)
        return mensaje
    def estadoBarraReserva(self):
        contador=0
        for campo in range(self.campos):
            if self.i["I"+str(campo+1)]==True and self.sbr["SBR"+str(campo+1)]==True:
                contador = contador +1
        if contador>=1:
            self.barraReserva=True
            print(f'La barra de Reserva esta en {self.barraReserva}')
            mensaje="La barra de Reserva esta en " +str(self.barraReserva)
        else:
            if self.barraPrincipal==True and self.intAcople==True:
                self.barraReserva=True
                print(f'La barra de Reserva esta en {self.barraReserva}')
                mensaje="La barra de Reserva esta en "+str(self.barraReserva)
            else:
                self.barraReserva=False
                print(f'La barra de Reserva esta en {self.barraReserva}')
                mensaje="La barra de Reserva esta en "+ str(self.barraReserva)
        return mensaje
    def accionSecSuperior(self,campo):
        if self.ss["SS"+str(campo)]==False:
            self.ss["SS"+str(campo)]=True
            print(f'El estado del seccionador es {self.ss["SS"+str(campo)]}')
            mensaje="El estado del seccionador es "+str(self.ss["SS"+str(campo)])
        else:
            if self.i["I"+str(campo)]==True:
                print(f'No se puede abrir porque el interruptor esta en {self.i["I"+str(campo)]}')
                mensaje="No se puede abrir porque el interruptor esta en "+str(self.i["I"+str(campo)])
            else:
                self.ss["SS"+str(campo)]=False
                print(f'El estado de seccionador es {self.ss["SS"+str(campo)]}')
                mensaje="El estado de seccionador es "+str(self.ss["SS"+str(campo)])
        return mensaje
    def accionSecBP(self,campo):
        if self.sbp["SBP"+str(campo)]==False:
            if self.i["I"+str(campo)]==True:
                if self.barraPrincipal==True:
                    if self.intAcople==True:
                        self.sbp["SBP"+str(campo)]=True
                        self.estadoBarraPrincipal()
                        self.estadoBarraReserva()
                        print(f'El estado del seccionador SBP esta en {self.sbp["SBP"+str(campo)]}')
                        mensaje="El estado del seccionador SBP esta en "+str(self.sbp["SBP"+str(campo)])
                    else:
                        print('No puede cerrar por diferencia de potencial')
                        mensaje="No puede cerrar por diferencia de potencial"
                else:
                    self.sbp["SBP"+str(campo)]=True
                    self.estadoBarraPrincipal()
                    self.estadoBarraReserva()
                    print(f'El estado del seccionador SBP esta en {self.sbp["SBP"+str(campo)]}')
                    mensaje="El estado del seccionador SBP esta en "+str(self.sbp["SBP"+str(campo)])
            else:
                self.sbp["SBP"+str(campo)]=True
                self.estadoBarraPrincipal()
                self.estadoBarraReserva()
                print(f'El estado del seccionador SBP esta en {self.sbp["SBP"+str(campo)]}')
                mensaje="El estado del seccionador SBP esta en "+str(self.sbp["SBP"+str(campo)])
        else:
            contador=0
            if self.i["I"+str(campo)]==True:
                if self.sbr["SBR"+str(campo)]==True:
                    if self.barraPrincipal==True:
                        if self.intAcople==True:
                            self.sbp["SBP"+str(campo)]=False
                            self.estadoBarraPrincipal()
                            self.estadoBarraReserva()
                            print(f'El estado del seccionador SBP esta en {self.sbp["SBP"+str(campo)]}')
                            mensaje="El estado del seccionador SBP esta en "+str(self.sbp["SBP"+str(campo)])
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
                                mensaje="No se puede accionar el Seccionador por diferencia de potencial"
                            else:
                                self.sbp["SBP"+str(campo)]=False
                                self.estadoBarraPrincipal()
                                self.estadoBarraReserva()
                                print(f'El estado del seccionador SBP esta en {self.sbp["SBP"+str(campo)]}')
                                mensaje="El estado del seccionador SBP esta en "+str(self.sbp["SBP"+str(campo)])
                    else:
                        self.sbp["SBP"+str(campo)]=False
                        self.estadoBarraPrincipal()
                        self.estadoBarraReserva()
                        print(f'El estado del seccionador SBP esta en {self.sbp["SBP"+str(campo)]}')
                        mensaje="El estado del seccionador SBP esta en "+str(self.sbp["SBP"+str(campo)])
                else:
                    print(f'No se puede accionar el Seccionador el interruptor {campo} esta en {self.i["I"+str(campo)]}')
                    mensaje="No se puede accionar el Seccionador el interruptor" +str(campo)+" esta en "+str(self.i["I"+str(campo)])
            else:
                self.sbp["SBP"+str(campo)]=False
                self.estadoBarraPrincipal()
                self.estadoBarraReserva()
                print(f'El estado del seccionador SBP esta en {self.sbp["SBP"+str(campo)]}')
                mensaje="El estado del seccionador SBP esta en "+str(self.sbp["SBP"+str(campo)])
        return mensaje
    def accionSecBR(self,campo):
        if self.sbr["SBR"+str(campo)]==False:
            if self.i["I"+str(campo)]==True:
                if self.barraReserva==True:
                    if self.intAcople==True:
                        self.sbr["SBR"+str(campo)]=True
                        self.estadoBarraPrincipal()
                        self.estadoBarraReserva()
                        print(f'El estado del seccionador SBR esta en {self.sbr["SBR"+str(campo)]}')
                        mensaje="El estado del seccionador SBR esta en "+str(self.sbr["SBR"+str(campo)])
                    else:
                        print('No puede cerrar por diferencia de potencial')
                        mensaje="No puede cerrar por diferencia de potencial"
                else:
                    self.sbr["SBR"+str(campo)]=True
                    self.estadoBarraPrincipal()
                    self.estadoBarraReserva()
                    print(f'El estado del seccionador SBP esta en {self.sbr["SBR"+str(campo)]}')
                    mensaje="El estado del seccionador SBP esta en "+str(self.sbr["SBR"+str(campo)])
            else:
                self.sbr["SBR"+str(campo)]=True
                self.estadoBarraPrincipal()
                self.estadoBarraReserva()
                print(f'El estado del seccionador SBR esta en {self.sbr["SBR"+str(campo)]}')
                mensaje="El estado del seccionador SBR esta en "+str(self.sbr["SBR"+str(campo)])
        else:
            contador=0
            if self.i["I"+str(campo)]==True:
                if self.sbp["SBP"+str(campo)]==True:
                    if self.barraPrincipal==True:
                        if self.intAcople==True:
                            self.sbr["SBR"+str(campo)]=False
                            self.estadoBarraPrincipal()
                            self.estadoBarraReserva()
                            print(f'El estado del seccionador SBR esta en {self.sbr["SBR"+str(campo)]}')
                            mensaje="El estado del seccionador SBR esta en "+str(self.sbr["SBR"+str(campo)])
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
                                mensaje="No se puede accionar el Seccionador por diferencia de potencial"
                            else:
                                self.sbr["SBR"+str(campo)]=False
                                self.estadoBarraPrincipal()
                                self.estadoBarraReserva()
                                print(f'El estado del seccionador SBR esta en {self.sbr["SBR"+str(campo)]}')
                                mensaje="El estado del seccionador SBR esta en "+str(self.sbr["SBR"+str(campo)])
                    else:
                        self.sbr["SBR"+str(campo)]=False
                        self.estadoBarraPrincipal()
                        self.estadoBarraReserva()
                        print(f'El estado del seccionador SBR esta en {self.sbr["SBR"+str(campo)]}')
                        mensaje="El estado del seccionador SBR esta en "+str(self.sbr["SBR"+str(campo)])
                else:
                    print(f'No se puede accionar el Seccionador el interruptor {campo} esta en {self.i["I"+str(campo)]}')
                    mensaje="No se puede accionar el Seccionador el interruptor"+str(campo) +" esta en "+ str(self.i["I"+str(campo)])
            else:
                self.sbr["SBR"+str(campo)]=False
                self.estadoBarraPrincipal()
                self.estadoBarraReserva()
                print(f'El estado del seccionador SBR esta en {self.sbr["SBR"+str(campo)]}')
                mensaje="El estado del seccionador SBR esta en "+str(self.sbr["SBR"+str(campo)])
        return mensaje
    def accionInterruptor(self,campo):
        if self.i["I"+str(campo)]==False:
            if self.ss["SS"+str(campo)]==True:
                if self.sbp["SBP"+str(campo)]==True:
                    if self.barraPrincipal==True:
                        if self.vs["VS"+str(campo)]==True:
                            self.i["I"+str(campo)]=True
                            self.estadoBarraPrincipal()
                            print(f'El interruptor {campo} esta en {self.i["I"+str(campo)]}')
                            mensaje="El interruptor "+ str(campo)+" esta en "+str(self.i["I"+str(campo)])
                        else:
                            print("Debe verificar sincronismo para cerrar el interruptor")
                            mensaje="Debe verificar sincronismo para cerrar el interruptor"
                    else:
                        self.i["I"+str(campo)]=True
                        self.estadoBarraPrincipal()
                        print(f'El interruptor {campo} esta en {self.i["I"+str(campo)]}')
                        mensaje="El interruptor " +str(campo) +" esta en " +str(self.i["I"+str(campo)])
                if self.sbr["SBR"+str(campo)]==True:
                    if self.barraReserva==True:
                        if self.vs["VS"+str(campo)]==True:
                            self.i["I"+str(campo)]=True
                            self.estadoBarraReserva()
                            print(f'El interruptor {campo} esta en {self.i["I"+str(campo)]}')
                            mensaje="El interruptor "+str(campo)+" esta en "+str(self.i["I"+str(campo)])
                        else:
                            print("Debe verificar sincronismo para cerrar el interruptor")
                            mensaje="Debe verificar sincronismo para cerrar el interruptor"
                    else:
                        self.i["I"+str(campo)]=True
                        self.estadoBarraReserva()
                        print(f'El interruptor {campo} esta en {self.i["I"+str(campo)]}')
                        mensaje="El interruptor "+str(campo)+" esta en "+str(self.i["I"+str(campo)])
                if self.sbp["SBP"+str(campo)]==False and self.sbr["SBR"+str(campo)]==False:
                    print("Debe cerrar alguno de los seccionadores de barras")
                    mensaje="Debe cerrar alguno de los seccionadores de barras"
            else:
                print("Debe cerrar los seccionadores adyacentes al interruptor {campo}")
                mensaje="Debe cerrar los seccionadores adyacentes al interruptor"+str(campo)
        else:
            self.i["I"+str(campo)]=False
            self.vs["VS"+str(campo)]=False
            self.estadoBarraReserva()
            self.estadoBarraPrincipal()
            print(f'El interruptor {campo} esta en {self.i["I"+str(campo)]}')
            mensaje="El interruptor "+str(campo)+" esta en "+str(self.i["I"+str(campo)])
        return mensaje
    def accionSecSupAcople(self):
        if self.ssAcople==False:
            self.ssAcople=True
            print(f'El estado del SS Acople es {self.ssAcople}')
            mensaje="El estado del SS Acople es "+str(self.ssAcople)
        else:
            if self.intAcople==True:
                print("No se puede accionat ya que el int Acople esta en {self.intAcople}")
                mensaje="No se puede accionat ya que el int Acople esta en "+str(self.intAcople)
            else:
                self.ssAcople=False
                print(f'El estado del SS Acople es {self.ssAcople}')
                mensaje="El estado del SS Acople es "+str(self.ssAcople)
        return mensaje
    def accionSecInfAcople(self):
        if self.siAcople==False:
            self.siAcople=True
            print(f'El estado del SI Acople es {self.siAcople}')
            mensaje="El estado del SI Acople es "+str(self.siAcople)
        else:
            if self.intAcople==True:
                print("No se puede accionar ya que el int Acople esta en {self.intAcople}")
                mensaje="No se puede accionar ya que el int Acople esta en "+str(self.intAcople)
            else:
                self.siAcople=False
                print(f'El estado del SI Acople es {self.siAcople}')
                mensaje="El estado del SI Acople es "+str(self.siAcople)
        return mensaje
    def accionIntAcople(self):
        contadorAC =0
        contadorCBP =0
        contadorCBR =0
        for  x in range(self.campos):
            if self.i["I"+str(x+1)]:
                if self.sbp["SBP"+str(x+1)] and self.sbr["SBR"+str(x+1)]:
                    contadorAC += 1
        for x in range(self.campos):
            if self.i["I"+str(x+1)]:
                if self.sbp["SBP"+str(x+1)]:
                    contadorCBP +=1
        for x in range(self.campos):
            if self.i["I"+str(x+1)]:
                if self.sbr["SBR"+str(x+1)]:
                    contadorCBR +=1
        if self.intAcople==False:
            if self.ssAcople==False or self.siAcople==False:
                print("Debe cerrar los seccionadores adyacentes")
                mensaje="Debe cerrar los seccionadores adyacentes"
            else:
                if contadorAC==0:
                    if contadorCBP>0:
                        if contadorCBR>0:
                            if self.vsAcople==False:
                                print("Debe verificar sincronismo")
                                mensaje="Debe verificar sincronismo"
                                print("Camino Barra R: ",contadorCBR)
                                print("Camino Barra P: ",contadorCBP)
                            else:
                                self.intAcople=True
                                self.estadoBarraPrincipal()
                                self.estadoBarraReserva()
                                print(f'El interruptor de acople esta en {self.intAcople}')
                                mensaje="El interruptor de acople esta en "+str(self.intAcople)
                        else:
                            self.intAcople=True
                            self.estadoBarraPrincipal()
                            self.estadoBarraReserva()
                            print(f'El interruptor de acople esta en {self.intAcople}')
                            mensaje="El interruptor de acople esta en "+str(self.intAcople)
                    else:
                        self.intAcople=True
                        self.estadoBarraPrincipal()
                        self.estadoBarraReserva()
                        print(f'El interruptor de acople esta en {self.intAcople}')
                        mensaje="El interruptor de acople esta en "+str(self.intAcople)
                else:
                    self.intAcople=True
                    self.estadoBarraPrincipal()
                    self.estadoBarraReserva()
                    print(f'El interruptor de acople esta en {self.intAcople}')
                    mensaje="El interruptor de acople esta en "+str(self.intAcople)
        else:
            self.intAcople=False
            self.estadoBarraPrincipal()
            self.estadoBarraReserva()
            print(f'El interruptor de acople esta en {self.intAcople}')
            mensaje="El interruptor de acople esta en "+str(self.intAcople)
        return mensaje
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
            mensaje="Se ha verificado Sincronismo"
        else:
            print("No es necesario verificar sincronismo")
            mensaje="No es necesario verificar sincronismo"
        return mensaje
    def accionVerIntAcople(self):
        if self.barraPrincipal==True and self.barraReserva==True:
            self.vsAcople=True
            print("Se ha verificado Sincronismo")
            mensaje="Se ha verificado Sincronismo"
        else:
            print("No es necesario verificar sincronismo")
            mensaje="No es necesario verificar sincronismo"
        return mensaje
prueba=dobleBarra(4)