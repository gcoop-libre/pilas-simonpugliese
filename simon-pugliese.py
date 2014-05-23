#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import time
import pilas
import piano
import partitura
import osvaldo

pilas.iniciar(usar_motor='qt', titulo='Simon pugliese', audio='pygame')

class Juego(pilas.escena.Base):

    def __init__(self):
        pilas.escena.Base.__init__(self)

    def iniciar(self):
        pilas.fondos.Fondo('img/fondo_juego.png')
        self.piano = piano.PianoNuevo(-240, -75)
        self.partitura = partitura.Partitura('partituras/la_yumba.csv')
        self.maestro = osvaldo.Osvaldo(self.partitura, self.piano)
        boton = BotonMenu(x=190, y=190, ruta_normal='salir_interno_normal.png', ruta_press='salir_interno_press.png', ruta_over='salir_interno_over.png')
        boton.conectar_presionado(pilas.terminar)


        self.notas_a_ejecutar = 1
        self.partitura.cortar_partitura(self.notas_a_ejecutar)
        self.maestro.interpretar()
        osvaldo.termine_de_evaluar.conectar(self.avanzar)

    def avanzar(self, datos_evento):
        if datos_evento['estuvo_bien']:
            self.maestro.decir('Bien! Sigamos...', True, False)
            self.notas_a_ejecutar += 1
            try:
                self.partitura.cortar_partitura(self.notas_a_ejecutar)
            except:
                # TODO: reproducir la canción original?
                self.maestro.decir('Felicitaciones!', True, False)
                return
        else:
            self.maestro.decir('Ups! Probemos de nuevo.', True, False)
            self.partitura.reiniciar()
        self.maestro.interpretar()

class Cancion:

    def __init__(self, ruta):
        self.sonido = pilas.musica.cargar(ruta)
        self.reproduciendo = False

    def reproducir(self, repetir = False):
        self.reproduciendo = True
        self.sonido.reproducir()

    def detener(self):
        self.reproduciendo = False
        self.sonido.detener()

    def esta_reproduciendo(self):
        return self.reproduciendo


class Mensaje(pilas.escena.Base):

    def __init__(self, archivo):
        self.archivo = archivo
        pilas.escena.Base.__init__(self)

    def iniciar(self):
        pilas.fondos.Color(pilas.colores.grisoscuro)
        self.cargar_texto()
        pilas.avisar("Pulsa ESC para regresar al menu.")

    def cargar_texto(self):
        texto = open(self.archivo, 'r').read().decode('utf8')
        self.texto = pilas.actores.Texto(texto, magnitud=15)
        self.texto.escala = 0
        self.texto.escala = [1], 0.25



class BotonMenu(pilas.actores.Boton):
    """Boton que cambia automáticamente de estado al presionarlo o pasar sobre él."""

    def __init__(self, x=0, y=0,
                ruta_normal='boton/boton_normal.png',
                ruta_press='boton/boton_press.png',
                ruta_over='boton/boton_over.png',
                ):
        pilas.actores.Boton.__init__(self, x=x, y=y, ruta_normal=ruta_normal, ruta_press=ruta_press, ruta_over=ruta_over)
        self.conectar_presionado(self.pintar_presionado)
        self.conectar_normal(self.pintar_normal)
        self.conectar_sobre(self.pintar_sobre)


class Menu(pilas.escena.Base):

    def __init__(self):
        pilas.escena.Base.__init__(self)

    def iniciar(self):
        pilas.fondos.Fondo('data/img/fondo.png')

        opciones = ['acerca', 'ayuda', 'salir']
        boton = BotonMenu(x=68, y=-80, ruta_normal='juego_normal.png', ruta_press='juego_press.png', ruta_over='juego_over.png')
        funcion = self.get_funcion('juego')
        boton.conectar_presionado(funcion)
        y = -140
        for opcion in opciones:
            y -=25
            img_normal = opcion + '_normal.png'
            img_press = opcion + '_press.png'
            img_over = opcion + '_over.png'
            boton = BotonMenu(x=-260, y=y, ruta_normal=img_normal, ruta_press=img_press, ruta_over=img_over)
            funcion = self.get_funcion(opcion)
            boton.conectar_presionado(funcion)

    def get_funcion(self, opcion):
        opciones = {
            'juego': self.iniciar_juego,
            'acerca': self.acerca_de,
            'ayuda': self.ayuda,
            'salir': self.salir
        }
        return opciones.get(opcion)

    def iniciar_juego(self):
        intro.detener()
        pilas.cambiar_escena(Juego())
        pilas.eventos.pulsa_tecla_escape.conectar(mostrar_menu)

    def acerca_de(self):
        pilas.cambiar_escena(Mensaje('data/txt/acerca_de.txt'))
        pilas.eventos.pulsa_tecla_escape.conectar(mostrar_menu)

    def ayuda(self):
        pilas.cambiar_escena(Mensaje('data/txt/ayuda.txt'))
        pilas.eventos.pulsa_tecla_escape.conectar(mostrar_menu)

    def salir(self):
        pilas.terminar()

def mostrar_menu(evento = None):
    if not intro.esta_reproduciendo():
        intro.reproducir()
    pilas.cambiar_escena(Menu())

intro = Cancion('data/la-yumba-intro.ogg')
mostrar_menu()
pilas.ejecutar()
