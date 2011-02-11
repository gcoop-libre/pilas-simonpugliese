#!-*- coding: utf-8 -*-
import tecla
import pilas

class PianoNuevo:
    
    def __init__(self, dx, dy):
        pilas.eventos.click_de_mouse.connect(self.cuando_hace_click)
        pilas.eventos.pulsa_tecla.conectar(self.presiona_nota_teclado)
        self.teclas = []
        self._crear_teclas(dx, dy)

    def _crear_teclas(self, dx, dy):
        ancho = 37
        contador = 0
        negras = [1, 3, 6, 8, 10]
        for nota in xrange(12, 36):
            if nota%12 in negras:
                color = 'negra'
                posicion_x = dx + (ancho * (contador) - ancho/2)
            else:
                color = 'blanca'
                posicion_x = dx + (ancho * contador)
                contador += 1
            
            self.teclas.append(tecla.Tecla(color, nota, posicion_x, dy))

                          
    def cuando_hace_click(self, evento):
        tecla = pilas.actores.utils.obtener_actor_en(evento.x, evento.y)

        if tecla and hasattr(tecla, 'pulsar'):
            tecla.pulsar()

    def presiona_nota_teclado(self, evento):
        mapa_teclas = { 
            u'z':0,
            u's':1,
            u'x':2,
            u'd':3,
            u'c':4,
            u'v':5,
            u'g':6,
            u'b':7,
            u'h':8,
            u'n':9,
            u'j':10,
            u'm':11,
            u',':12,
            u'l':13,
            u'.':14,
            u'ñ':15,
            u'-':16,
            }
        numero_tecla = mapa_teclas.get(evento.codigo, None)
        if numero_tecla != None:
            self.teclas[numero_tecla].pulsar()
        
        

        

