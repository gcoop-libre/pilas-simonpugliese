import pilas
import piano

from pilas.actores import Animado

class Tecla(Animado):

    def __init__(self, grilla, nota, posicion):
        Animado.__init__(self, grilla)
        self.sonido = pilas.sonidos.cargar('c.wav')
        afinacion = 2 ** (nota / 12.0) #para no importar math 
        self.sonido.definir_pitch(afinacion)
        self.x = -300  + posicion * 23

    def pulsar(self):
        self.definir_cuadro(1)
        self.sonido.reproducir()
        pilas.mundo.agregar_tarea(0.5, self.restaurar)

    def restaurar(self):
        self.definir_cuadro(0)


class Piano:
    """Representa el piano que tiene teclas y carga los sonidos.

    El piano recibe los clicks del usuario y le avisa a las teclas
    sobre la cual se ha pulsado."""

    def __init__(self):
        pilas.eventos.click_de_mouse.connect(self.cuando_hace_click)
        self.crear_piezas()

    def crear_piezas(self):
        grilla = pilas.imagenes.cargar_grilla("data/tecla.png", 2, 1)
        grilla.escala = 0.5
        for numero_nota in xrange(12, 37):
            posicion = numero_nota - 12
            Tecla(grilla, numero_nota, posicion)

    def cuando_hace_click(self, evento):
        tecla = pilas.actores.utils.obtener_actor_en(evento.x, evento.y)

        if tecla and hasattr(tecla, 'pulsar'):
            tecla.pulsar()


pilas.iniciar(titulo='Simon pugliese')



pilas.avisar('Usa alt+q para salir.')
pilas.fondos.Pasto()
a = Piano()

b = piano.PianoNuevo(-200, 200)



pilas.ejecutar()


