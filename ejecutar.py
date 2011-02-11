import pilas
from pilas.actores import Animado

class Tecla(Animado):

    def __init__(self, grilla, nota, posicion):
        Animado.__init__(self, grilla)
        self.sonido = pilas.sonidos.cargar(nota + '.wav')
        self.x = 160 - posicion * 55

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
        Tecla(grilla, 'c', 0)
        Tecla(grilla, 'd', 1)
        Tecla(grilla, 'e', 2)
        Tecla(grilla, 'f', 3)
        Tecla(grilla, 'g', 4)
        Tecla(grilla, 'a', 5)
        Tecla(grilla, 'b', 6)

    def cuando_hace_click(self, evento):
        tecla = pilas.actores.utils.obtener_actor_en(evento.x, evento.y)

        if tecla:
            tecla.pulsar()



pilas.iniciar(titulo='Pianito')
pilas.avisar('Use la tecla "q" para salir.')

a = Piano()
pilas.ejecutar()


