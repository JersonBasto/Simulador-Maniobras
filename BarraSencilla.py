# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class barraSencilla:
    def __init__(self,campos):
        self.campos=campos
        self.i={}
        self.ss={}
        self.si={}
        self.vs={}
        self.barraPrincipal=False
        for campo in range (campos):
            self.i["I"+str(campo+1)]=False
            self.ss["SS"+str(campo+1)]=False
            self.si["SI"+str(campo+1)]=False
            self.vs["VI"+str(campo+1)]=False
    def estadoBarra(self):
        if True in self.i.values():
            self.barraPrincipal=True
            print(f'La Barra se encuentra en {self.barraPrincipal}')
            mensaje="La Barra se encuentra en" + str(self.barraPrincipal)
        else:
            self.barraPrincipal=False
            print(f'La Barra se encuentra en {self.barraPrincipal}')
            mensaje="La Barra se encuentra en " + str(self.barraPrincipal)
        return mensaje
    def accionInterruptor(self,campo):
        if self.i["I"+str(campo)]==False:
            if self.ss["SS"+str(campo)]==False or self.si["SI"+str(campo)]==False:
                print(f'El estado del Interruptor es {self.i["I"+str(campo)]}')
                print("Debe cerrar los seccionadores adyacentes al interruptor")
                mensaje="Debe cerrar los seccionadores adyacentes al interruptor"
            else:
                if self.barraPrincipal==True:
                    if self.vs["VI"+str(campo)]==True:
                        self.i["I"+str(campo)]=True
                        print(f'El estado del Interruptor es {self.i["I"+str(campo)]}')
                        mensaje="El estado del Interruptor es "+str(self.i["I"+str(campo)])
                    else:
                        print("No se puede cerrar el interruptor, debe verificar sincronismo")
                        mensaje="No se puede cerrar el interruptor, debe verificar sincronismo"
                else:
                    self.i["I"+str(campo)]=True
                    self.estadoBarra()
                    print(f'El estado del Interruptor es {self.i["I"+str(campo)]}')
                    mensaje="El estado del Interruptor es "+str(self.i["I"+str(campo)])
        else:
            self.i["I"+str(campo)]=False
            self.vs["VI"+str(campo)]=False
            self.estadoBarra()
            print(f'El estado del Interruptor es {self.i["I"+str(campo)]}')
            mensaje="El estado del Interruptor es "+str(self.i["I"+str(campo)])
        return mensaje
    def verificarSincronismo(self,campo):
        if self.vs["VI"+str(campo)]==False and self.barraPrincipal==True:
            if self.i["I"+str(campo)]==False:
                if self.ss["SS"+str(campo)]==False or self.si["SI"+str(campo)]==False:
                    print("Debe cerrar los seccionadores")
                    mensaje="Debe cerrar los seccionadores"
                else:
                    self.vs["VI"+str(campo)]=True
                    print(f'El estado de verificacion es {self.vs["VI"+str(campo)]}')
                    mensaje="El estado de verificacion es "+str(self.vs["VI"+str(campo)])
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
    def accionSecSuperior(self,campo):
        if self.ss["SS"+str(campo)]==False:
            self.ss["SS"+str(campo)]=True
            print(f'El seccionador superior {campo} esta en estado {self.ss["SS"+str(campo)]}')
            mensaje="El seccionador superior "+str(campo) +" esta en estado "+str(self.ss["SS"+str(campo)])
        else:
            if self.i["I"+str(campo)]==True:
                print("No se puede abrir el seccionador ya que el interruptor esta cerrado")
                mensaje="No se puede abrir el seccionador ya que el interruptor esta cerrado"
            else:
                self.ss["SS"+str(campo)]=False
                print(f'El seccionador superior {campo} esta en estado {self.ss["SS"+str(campo)]}')
                mensaje="El seccionador superior " +str(campo) +" esta en estado " +str(self.ss["SS"+str(campo)])
        return mensaje
    def accionSecInferior(self,campo):
        if self.si["SI"+str(campo)]==False:
            self.si["SI"+str(campo)]=True
            print(f'El seccionador Inferior {campo} esta en estado {self.si["SI"+str(campo)]}')
            mensaje="El seccionador Inferior "+str(campo) +" esta en estado "+str(self.si["SI"+str(campo)])
        else:
            if self.i["I"+str(campo)]==True:
                print("No se puede abrir el seccionador ya que el interruptor esta cerrado")
                mensaje="No se puede abrir el seccionador ya que el interruptor esta cerrado"
            else:
                self.si["SI"+str(campo)]=False
                print(f'El seccionador Inferior {campo} esta en estado {self.si["SI"+str(campo)]}')
                mensaje="El seccionador superior " +str(campo) +" esta en estado " +str(self.si["SI"+str(campo)])
        return mensaje