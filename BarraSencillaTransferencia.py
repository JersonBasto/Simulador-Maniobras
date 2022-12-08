# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 14:51:10 2022

@author: j_dbg
"""

class BarraSencillaTransferencia:
    def __init__(self,campos):
        self.campos=campos
        self.i={}
        self.ss={}
        self.si={}
        self.st={}
        self.vs={}
        self.et={}
        self.barraPrincipal=False
        self.barraTransferencia=False
        self.intAcople=False
        self.ssAcople=False
        self.siAcople=False
        for campo in range(campos):
            self.i["I"+str(campo+1)]=False
            self.ss["SS"+str(campo+1)]=False
            self.si["SI"+str(campo+1)]=False
            self.st["ST"+str(campo+1)]=False
            self.vs["VS"+str(campo+1)]=False
            self.et["ET"+str(campo+1)]=True
    def estadoBarraPrincipal(self):
        contador=0
        for campo in range(self.campos):
            if self.i["I"+str(campo+1)]==True and self.et["ET"+str(campo+1)]==True:
                self.barraPrincipal=True
                contador=contador+1
                print(f'El estado de la barra es {self.barraPrincipal}')
                mensaje="El estado de la barra es " +str(self.barraPrincipal)
        if contador==0:
            self.barraPrincipal=False
            print(f'El estado de la barra es {self.barraPrincipal}')
            mensaje="El estado de la barra es " +str(self.barraPrincipal)
        self.estadoBarraTransferencia()
        if self.barraTransferencia==True and self.intAcople==True:
            self.barraPrincipal=True
            print(f'El estado de la barra es {self.barraPrincipal}')
            mensaje="El estado de la barra es " +str(self.barraPrincipal)
        return mensaje
    def estadoBarraTransferencia(self):
        contador=0
        for campo in range(self.campos):
            if self.et["ET"+str(campo+1)]==True and self.st["ST"+str(campo+1)]==True:
                self.barraTransferencia=True
                contador=contador+1
                print(f'El estado de la barra de transferencia es {self.barraTransferencia}')
                mensaje="El estado de la barra de transferencia es "+str(self.barraTransferencia)
        if contador==0:
            self.barraTransferencia=False
            print(f'El estado de la barra de transferencia es {self.barraTransferencia}')
            mensaje="El estado de la barra de transferencia es "+str(self.barraTransferencia)
        if self.barraPrincipal==True and self.intAcople==True:
            self.barraTransferencia=True
            print(f'El estado de la barra de transferencia es {self.barraTransferencia}')
            mensaje="El estado de la barra de transferencia es "+str(self.barraTransferencia)
        return mensaje
    def accionSecSuperior(self,campo):
        if self.ss["SS"+str(campo)]==False:
            self.ss["SS"+str(campo)]=True
            print(f'El seccionador superior de {campo} esta en {self.ss["SS"+str(campo)]}')
            mensaje="El seccionador superior de " +str(campo)+" esta en "+str(self.ss["SS"+str(campo)])
        else:
            if self.i["I"+str(campo)]==False:
                self.ss["SS"+str(campo)]=False
                print(f'El seccionador superior de {campo} esta en {self.ss["SS"+str(campo)]}')
                mensaje="El seccionador superior de "+str(campo)+ " esta en " +str(self.ss["SS"+str(campo)])
            else:
                print(f'No se puede abrir el seccionador ya que el interruptor esta en {self.i["I"+str(campo)]}')
                mensaje="No se puede abrir el seccionador ya que el interruptor esta en " +str(self.i["I"+str(campo)])
        return mensaje
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
    def accionInterruptor(self,campo):
        if self.i["I"+str(campo)]==False:
            if self.ss["SS"+str(campo)]==True and self.si["SI"+str(campo)]==True:
                if self.st["ST"+str(campo)]==True:
                    self.estadoBarraPrincipal()
                    if self.barraPrincipal==True and self.et["ET"+str(campo)]:
                        self.estadoBarraTransferencia()
                        if self.barraTransferencia==True:
                            if self.intAcople==True:
                                self.i["I"+str(campo)]=True
                                print(f'El estado del interruptor {campo} es {self.i["I"+str(campo)]}')
                                mensaje="El estado del interruptor "+str(campo)+" es "+str(self.i["I"+str(campo)])
                            else:
                                if self.vs["VS"+str(campo)]==True:
                                    self.i["I"+str(campo)]=True
                                    print(f'El estado del interruptor {campo} es {self.i["I"+str(campo)]}')
                                    mensaje="El estado del interruptor "+str(campo)+" es "+str(self.i["I"+str(campo)])
                                else:
                                    print(f"Debe verificar sincronismo en el interruptor {campo}")
                                    mensaje="Debe verificar sincronismo en el interruptor "+str(campo)
                        else:
                            if self.vs["VS"+str(campo)]==True:
                                self.i["I"+str(campo)]=True
                                print(f'El estado del interruptor {campo} es {self.i["I"+str(campo)]}')
                                mensaje="El estado del interruptor "+str(campo)+" es "+str(self.i["I"+str(campo)])
                            else:
                                print(f"Debe verificar sincronismo en el interruptor {campo}")
                                mensaje="Debe verificar sincronismo en el interruptor "+str(campo)
                    else:
                        self.i["I"+str(campo)]=True
                        print(f'El estado del interruptor {campo} es {self.i["I"+str(campo)]}')
                        mensaje="El estado del interruptor "+str(campo)+" es "+str(self.i["I"+str(campo)])
                        self.estadoBarraPrincipal()
                        self.estadoBarraTransferencia()
                else:
                    self.estadoBarraPrincipal()
                    if self.barraPrincipal==True and self.et["ET"+str(campo)]:
                        if self.vs["VS"+str(campo)]==True:
                            self.i["I"+str(campo)]=True
                            print(f'El estado del interruptor {campo} es {self.i["I"+str(campo)]}')
                            mensaje="El estado del interruptor "+str(campo)+" es "+str(self.i["I"+str(campo)])
                            self.estadoBarraPrincipal()
                            self.estadoBarraTransferencia()
                        else:
                            print("Debe verificar sincronismo antes de cerrar")
                            mensaje="Debe verificar sincronismo antes de cerrar"
                    else:
                        self.i["I"+str(campo)]=True
                        print(f'El estado del interruptor {campo} es {self.i["I"+str(campo)]}')
                        mensaje="El estado del interruptor "+str(campo)+" es "+str(self.i["I"+str(campo)])
                        self.estadoBarraPrincipal()
                        self.estadoBarraTransferencia()
            else:
                print("Debe cerrar los seccionadores adyacentes")
                mensaje="Debe cerrar los seccionadores adyacentes"
        else:
            self.i["I"+str(campo)]=False
            self.vs["VS"+str(campo)]=False
            self.estadoBarraPrincipal()
            self.estadoBarraTransferencia()
            print(f'El estado del interruptor {campo} es {self.i["I"+str(campo)]}')
            mensaje="El estado del interruptor "+str(campo)+" es "+str(self.i["I"+str(campo)])
        return mensaje
    def accionIntAcople(self):
        contador=0
        for x in range(self.campos):
            if self.st["ST"+str(x+1)]:
                contador+=1

        if contador>=1:
            mensaje="No puede realziar esta operacion, el Seccionador de transferencia esta en modo de Puente de paso"
            print(mensaje)
        else:
            if self.intAcople==False:
                if self.siAcople==True and self.ssAcople==True:
                    self.intAcople=True
                    self.estadoBarraPrincipal()
                    self.estadoBarraTransferencia()
                    print(f'El estado del interruptor es {self.intAcople}')
                    mensaje="El estado del interruptor es "+str(self.intAcople)
                else:
                    print("Debe cerrar los seccionadores adyacentes")
                    mensaje="Debe cerrar los seccionadores adyacentes"
            else:
                self.intAcople=False
                self.estadoBarraPrincipal()
                self.estadoBarraTransferencia()
                print(f'El estado del interruptor es {self.intAcople}')
                mensaje="El estado del interruptor es "+str(self.intAcople)
        return mensaje
    def accionSecTransferencia(self,campo):
        contador=0
        if self.st["ST"+str(campo)]==False:
            if True in self.st.values():
                if self.barraPrincipal==False and self.intAcople==False:
                    for x in range(self.campos):
                        if self.st["ST"+str(x+1)]==True:
                            contador= contador+1
                    if contador<=1:
                        self.st["ST"+str(campo)]=True
                        self.estadoBarraPrincipal()
                        self.estadoBarraTransferencia()
                        print(f'El estado del seccionador de transferencia es {self.st["ST"+str(campo)]}')
                        mensaje="El estado del seccionador de transferencia es "+str(self.st["ST"+str(campo)])
                    else:
                        print("Solamente se puede usar 2 en el puente de paso")
                        mensaje="Solamente se puede usar 2 en el puente de paso"
                else:
                    print("La barra solo puede soportar un campo de linea")
                    mensaje="La barra solo puede soportar un campo de linea"
            else:
                if self.intAcople==True:
                    if self.i["I"+str(campo)]==False:
                        if self.barraTransferencia==True and self.et["ET"+str(campo)]==True:
                            print("No se puede cerrar el seccionador ya que hay diferencia de potencial")
                            mensaje="No se puede cerrar el seccionador ya que hay diferencia de potencial"
                        else:
                            self.st["ST"+str(campo)]=True
                            self.estadoBarraPrincipal()
                            self.estadoBarraTransferencia()
                            print(f'El estado del seccionador de transferencia es {self.st["ST"+str(campo)]}')
                            print("Se transfirieron las protecciones")
                            mensaje="El estado del seccionador de transferencia es "+str(self.st["ST"+str(campo)])+"\n"+"Se transfirieron las protecciones"
                    else:
                        self.st["ST"+str(campo)]=True
                        self.estadoBarraPrincipal()
                        self.estadoBarraTransferencia()
                        print(f'El estado del seccionador de transferencia es {self.st["ST"+str(campo)]}')
                        print("Se transfirieron las protecciones")
                        mensaje="El estado del seccionador de transferencia es "+str(self.st["ST"+str(campo)])+"\n"+"Se transfirieron las protecciones"
                else:
                    if self.barraPrincipal==True:
                        print("Debe cerrar es interruptor de acople para transferir protecciones")
                        mensaje="Debe cerrar es interruptor de acople para transferir protecciones"
                    elif self.barraTransferencia==True:
                        self.st["ST"+str(campo)]=True
                        self.estadoBarraPrincipal()
                        self.estadoBarraTransferencia()
                        print(f'El estado del seccionador de transferencia es {self.st["ST"+str(campo)]}')
                        mensaje="El estado del seccionador de transferencia es "+str(self.st["ST"+str(campo)])
                    else:
                        if self.intAcople:
                            mensaje="Debe abrir el Interruptor de acople para iniciar puente de paso"
                        else:
                            self.st["ST"+str(campo)]=True
                            self.estadoBarraPrincipal()
                            self.estadoBarraTransferencia()
                            print(f'El estado del seccionador de transferencia es {self.st["ST"+str(campo)]}')
                            print('Inicio de puente de paso')
                            mensaje="El estado del seccionador de transferencia es "+str(self.st["ST"+str(campo)])+"\n"+"Inicio de puente de paso"
        else:
            if self.i["I"+str(campo)]==True:
                self.st["ST"+str(campo)]=False
                self.estadoBarraPrincipal()
                self.estadoBarraTransferencia()
                print(f'El estado del seccionador de transferencia es {self.st["ST"+str(campo)]}')
                mensaje="El estado del seccionador de transferencia es "+str(self.st["ST"+str(campo)])
            else:
                if self.et["ET"+str(campo)]==True:
                    if self.intAcople==True and self.barraPrincipal==True:
                        if True in self.i.values():
                            print("No se puede realizar la operacion entraria en diferencia de potencial")
                            mensaje="No se puede realizar la operacion entraria en diferencia de potencial"
                        else:
                            self.st["ST"+str(campo)]=False
                            self.estadoBarraPrincipal()
                            self.estadoBarraTransferencia()
                            print(f'El estado del seccionador de transferencia es {self.st["ST"+str(campo)]}') 
                            mensaje="El estado del seccionador de transferencia es "+str(self.st["ST"+str(campo)])
                    else:
                        self.st["ST"+str(campo)]=False
                        self.estadoBarraPrincipal()
                        self.estadoBarraTransferencia()
                        print(f'El estado del seccionador de transferencia es {self.st["ST"+str(campo)]}')
                        mensaje="El estado del seccionador de transferencia es "+str(self.st["ST"+str(campo)])
                else:
                    self.st["ST"+str(campo)]=False
                    self.estadoBarraPrincipal()
                    self.estadoBarraTransferencia()
                    print(f'El estado del seccionador de transferencia es {self.st["ST"+str(campo)]}')
                    mensaje="El estado del seccionador de transferencia es "+str(self.st["ST"+str(campo)])
        return mensaje
    def verificarSincronismo(self,campo):
        if self.vs["VS"+str(campo)]==False and self.barraPrincipal==True:
            if self.i["I"+str(campo)]==False:
                if self.ss["SS"+str(campo)]==False or self.si["SI"+str(campo)]==False:
                    print("Debe cerrar los seccionadores")
                    mensaje="Debe cerrar los seccionadores"
                else:
                    self.vs["VS"+str(campo)]=True
                    print(f'El estado de verificacion es {self.vs["VS"+str(campo)]}')
                    mensaje="El estado de verificacion es "+str(self.vs["VS"+str(campo)])
            else:
                print("No se puede verificar sincronismo, el interruptor ya esta cerrado")
                mensaje="No se puede verificar sincronismo, el interruptor ya esta cerrado"
        else:
            if self.i["I"+str(campo)]==True:
                print("No se puede verificar sincronismo, el interruptor ya esta cerrado")
                mensaje="No se puede verificar sincronismo, el interruptor ya esta cerrado"
            else:
                print("No es necesario verificar sincronismo ya que la barra no esta energizada")
                mensaje="No es necesario verificar sincronismo ya que la barra no esta energizada"
        return mensaje
    def accionSecSupAcople(self):
        if self.ssAcople==False:
            self.ssAcople=True
            print(f'El seccionador superior del campo de acople esta en {self.ssAcople}')
            mensaje="El seccionador superior del campo de acople esta en " +str(self.ssAcople)
        else:
            if self.intAcople==False:
                self.ssAcople=False
                print(f'El seccionador superior del campo de acople esta en {self.ssAcople}')
                mensaje="El seccionador superior del campo de acople esta en " +str(self.ssAcople)
            else:
                print(f'No se puede abrir el seccionador ya que el interruptor esta en {self.intAcople}')
                mensaje="No se puede abrir el seccionador ya que el interruptor esta en "+str(self.intAcople)
        return mensaje
    def accionSecInfAcople(self):
        if self.siAcople==False:
            self.siAcople=True
            print(f'El seccionador inferior del campo de acople esta en {self.ssAcople}')
            mensaje="El seccionador inferior del campo de acople esta en " +str(self.siAcople)
        else:
            if self.intAcople==False:
                self.siAcople=False
                print(f'El seccionador inferior del campo de acople esta en {self.ssAcople}')
                mensaje="El seccionador inferior del campo de acople esta en " +str(self.siAcople)
            else:
                print(f'No se puede abrir el seccionador ya que el interruptor esta en {self.intAcople}')
                mensaje="No se puede abrir el seccionador ya que el interruptor esta en "+str(self.intAcople)
        return mensaje
    def accionExtremo(self,campo):
        if self.et["ET"+str(campo)]==True:
            self.et["ET"+str(campo)]=False
            self.estadoBarraPrincipal()
            self.estadoBarraTransferencia()
            mensaje="Se abre Extremo "+str(campo)
            print(mensaje)
        else:
            if self.barraPrincipal:
                if self.barraTransferencia and self.st["ST"+str(campo)]:
                    self.et["ET"+str(campo)]=True
                    self.estadoBarraPrincipal()
                    self.estadoBarraTransferencia()
                    mensaje="Se cierra Extremo "+str(campo)+" verificando Sincronismo"
                    print(mensaje)
                else:
                    mensaje="Se cierra Extremo "+str(campo)+" verificando Sincronismo"
                    self.et["ET"+str(campo)]=True
                    self.estadoBarraPrincipal()
                    self.estadoBarraTransferencia()
                    print(mensaje)
            else:
                mensaje="Se cierra Extremo "+str(campo)
                self.et["ET"+str(campo)]=True
                self.estadoBarraPrincipal()
                self.estadoBarraTransferencia()
                print(mensaje)
        return mensaje
prueba=BarraSencillaTransferencia(4)