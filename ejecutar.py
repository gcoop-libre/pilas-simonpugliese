# -*- encoding: utf-8 -*-
import time
import pilas
import piano
import partitura
import osvaldo

pilas.iniciar(usar_motor='qt', titulo='Simon pugliese')

class Juego(pilas.escena.Base):

    def __init__(self):
        pilas.escena.Base.__init__(self)

    def iniciar(self):
        pilas.fondos.Pasto()
        self.piano = piano.PianoNuevo(-240, -75)
        self.partitura = partitura.Partitura('partituras/la_yumba.csv')
        self.maestro = osvaldo.Osvaldo(self.partitura, self.piano)
        self.notas_a_ejecutar = 1
        self.partitura.cortar_partitura(self.notas_a_ejecutar)
        self.maestro.interpretar()
        osvaldo.termine_de_evaluar.conectar(self.avanzar)

    def avanzar(self, datos_evento):
        if datos_evento['estuvo_bien']:
            self.maestro.decir('Bien! Sigamos...')
            self.notas_a_ejecutar += 1
            try:
                self.partitura.cortar_partitura(self.notas_a_ejecutar)
            except:
                # TODO: reproducir la canción original?
                self.maestro.decir('Felicitaciones!')
                return
        else:
            self.maestro.decir('Ups! Probemos de nuevo.')
            self.partitura.reiniciar()
        time.sleep(2)
        self.maestro.interpretar()

class Menu(pilas.escena.Base):

    def __init__(self):
        pilas.escena.Base.__init__(self)

    def iniciar(self):
        pilas.fondos.Noche()
        m = pilas.actores.Menu([
                ("Jugar", iniciar_juego),
                ("Acerca de...", acerca_de),
                ("Ayuda", ayuda),
                ("Salir", salir),
            ])
        m.escala = 0
        m.escala = [1], 0.25


class Ayuda(pilas.escena.Base):

    def __init__(self):
        pilas.escena.Base.__init__(self)

    def iniciar(self):
        pilas.fondos.Color(pilas.colores.grisoscuro)
        texto = pilas.actores.Texto("Escena no disponible...")
        pilas.avisar("Pulsa ESC para regresar al menu.")

class AcercaDe(pilas.escena.Base):

    def __init__(self):
        pilas.escena.Base.__init__(self)

    def iniciar(self):
        pilas.fondos.Color(pilas.colores.grisoscuro)
        self.cargar_texto()
        pilas.avisar("Pulsa ESC para regresar al menu.")

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


def mostrar_menu(evento = None):
    pilas.cambiar_escena(Menu())

def iniciar_juego():
    pilas.cambiar_escena(Juego())
    pilas.eventos.pulsa_tecla_escape.conectar(mostrar_menu)

def acerca_de():
    pilas.cambiar_escena(AcercaDe())
    pilas.eventos.pulsa_tecla_escape.conectar(mostrar_menu)

def ayuda():
    pilas.cambiar_escena(Ayuda())
    pilas.eventos.pulsa_tecla_escape.conectar(mostrar_menu)

def salir():
    pilas.terminar()


mostrar_menu()
pilas.ejecutar()
