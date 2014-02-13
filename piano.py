#!-*- coding: utf-8 -*-
import tecla
import pilas

class PianoNuevo:

    def __init__(self, dx, dy):
        pilas.eventos.termina_click.conectar(self.cuando_hace_click)
        self.teclas = {}
        pilas.eventos.pulsa_tecla.conectar(self.presiona_nota_teclado)
        self._crear_teclas(dx, dy)

    def _crear_teclas(self, dx, dy):
        ancho = 37
        contador = 0
        octavas = 2

        for octava in range(1, octavas + 1):
            for nota in ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']:
                if nota.find("#") != -1:
                    color = 'negra'
                    posicion_x = dx + (ancho * (contador) - ancho/2)
                else:
                    color = 'blanca'
                    posicion_x = dx + (ancho * contador)
                    contador += 1

                nombre_nota = "%s%d" % (nota, octava)
                self.teclas[nombre_nota] = tecla.Tecla(color, nombre_nota, posicion_x, dy)

    def cuando_hace_click(self, evento):
        tecla = pilas.actores.utils.obtener_actor_en(evento.x, evento.y)

        if tecla and hasattr(tecla, 'pulsar'):
            tecla.pulsar()

    def reproducir_nota(self, nota):
        self.teclas[nota].pulsar()

    def presiona_nota_teclado(self, evento):
        mapa_teclas = {
            'z':'C1',
            's':'C#1',
            'x':'D1',
            'd':'D#1',
            'c':'E1',
            'v':'F1',
            'g':'F#1',
            'b':'G1',
            'h':'G#1',
            'n':'A1',
            'j':'A#1',
            'm':'B1',
            ',':'C2',
            'l':'C#2',
            '.':'D2',
            'ñ':'D#2',
            '-':'E2',
            }

        numero_tecla = mapa_teclas.get(evento.texto, None)

        if numero_tecla != None:
            self.teclas[numero_tecla].pulsar()
