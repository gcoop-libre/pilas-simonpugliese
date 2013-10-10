# -*- encoding: utf-8 -*-
import pilas
import piano
from interprete import Interprete
import partitura
import osvaldo

from pilas.actores import Animado

pilas.iniciar(usar_motor='qt', titulo='Simon pugliese')

class Juego(pilas.escena.Base):

    def __init__(self):
        pilas.escena.Base.__init__(self)
        pilas.fondos.Pasto()

        b = piano.PianoNuevo(-240, -75)
        t = osvaldo.Osvaldo()
        p = partitura.Partitura('partituras/la_yumba.csv')

        interprete = Interprete(p, b)


class Menu(pilas.escena.Base):

    def __init__(self):
        pilas.escena.Base.__init__(self)
        pilas.fondos.Noche()
        m = pilas.actores.Menu([
                ("Jugar", self.iniciar_juego),
                ("Acerca de...", self.acerca_de),
                ("Ayuda", Ayuda),
                ("Salir", self.salir),
            ])
        m.escala = 0
        m.escala = [1], 0.25

    def iniciar_juego(self):
        Juego()

    def acerca_de(self):
        AcercaDe()

    def ayuda(self):
        Ayuda()

    def salir(self):
        pilas.terminar()


class Ayuda(pilas.escena.Base):

    def __init__(self):
        pilas.escena.Base.__init__(self)
        pilas.fondos.Color(pilas.colores.grisoscuro)
        texto = pilas.actores.Texto("Escena no disponible...")
        pilas.eventos.pulsa_tecla_escape.conectar(self.pulsa_tecla)
        pilas.avisar("Pulsa ESC para regresar al menu.")

    def pulsa_tecla(self, evento):
        Menu()

class AcercaDe(pilas.escena.Base):

    def __init__(self):
        pilas.escena.Base.__init__(self)
        pilas.fondos.Color(pilas.colores.grisoscuro)
        self.cargar_texto()
        pilas.eventos.pulsa_tecla_escape.conectar(self.pulsa_tecla)
        pilas.avisar("Pulsa ESC para regresar al menu.")

    def pulsa_tecla(self, evento):
        Menu()

    def cargar_texto(self):
        texto = u"""
Simon Pugliese es un juego de memoria visual.

Es un homenaje al Maestro Osvaldo Pugliese
realizado por integrantes de la
Cooperativa gcoop. El jugador
deberá seguir la secuencia de teclas del piano
para componer las melodias del maestro Pugliese,
al estilo del famoso juego Simon.

Simon Pugliese está desarrollado con la herramienta
Pilas Engine.
        """

        self.texto = pilas.actores.Texto(texto, magnitud=15)
        self.texto.y = [275],0.5
        self.texto.aprender(pilas.habilidades.Arrastrable)


Menu()
pilas.ejecutar()
