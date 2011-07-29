#!-*- coding: utf-8 -*-
import tecla
import pilas

class PianoNuevo:
    
    def __init__(self, dx, dy):
        pilas.eventos.click_de_mouse.connect(self.cuando_hace_click)
        self.teclas = {}
        pilas.eventos.pulsa_tecla.conectar(self.presiona_nota_teclado)
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
            
            self.teclas[nota] = tecla.Tecla(color, nota, posicion_x, dy)

    def cuando_hace_click(self, evento):
        tecla = pilas.actores.utils.obtener_actor_en(evento.x, evento.y)

        if tecla and hasattr(tecla, 'pulsar'):
            tecla.pulsar()

    def reproducir_nota(self, nota):
        self.teclas[nota].pulsar()

    def presiona_nota_teclado(self, evento):
        mapa_teclas = { 
            u'z':12,
            u's':13,
            u'x':14,
            u'd':15,
            u'c':16,
            u'v':17,
            u'g':18,
            u'b':19,
            u'h':20,
            u'n':21,
            u'j':22,
            u'm':23,
            u',':24,
            u'l':25,
            u'.':26,
            u'ñ':27,
            u'-':28,
            }

        numero_tecla = mapa_teclas.get(evento.codigo, None)

        if numero_tecla != None:
            self.teclas[numero_tecla].pulsar()
