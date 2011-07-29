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
            'z':12,
            's':13,
            'x':14,
            'd':15,
            'c':16,
            'v':17,
            'g':18,
            'b':19,
            'h':20,
            'n':21,
            'j':22,
            'm':23,
            ',':24,
            'l':25,
            '.':26,
            'ñ':27,
            '-':28,
            }

        numero_tecla = mapa_teclas.get(evento.texto, None)

        if numero_tecla != None:
            self.teclas[numero_tecla].pulsar()
