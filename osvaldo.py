import time
import pilas
from interprete import Interprete, termine_de_tocar
from tecla import tecla_pulsada

termine_de_evaluar = pilas.evento.Evento("Evaluacion terminada")

class Osvaldo(pilas.actores.Actor):

    def __init__(self, partitura, piano, x=0, y=0):
        pilas.actores.Actor.__init__(self, "img/osvaldo.png")
        self.x = 100
        self.y = 100
        self.decir("A ver si me podes seguir...")
        self.escala = 0.5
        self.partitura = partitura
        self.piano = piano

    def interpretar(self):
       self.interprete = Interprete(self.partitura, self.piano)
       termine_de_tocar.conectar(self.evaluar, 'interpretando')

    def evaluar(self, datos_evento):
        time.sleep(2)
        self.decir("Ahora te toca ti...")
        self.partitura.reiniciar()
        self.siguiente_nota = self.partitura.siguiente()[1]
        self.ultima_nota = False
        termine_de_tocar.desconectar_por_id('interpretando')
        tecla_pulsada.conectar(self.evaluar_tecla, 'evaluando')

    def evaluar_tecla(self, datos_evento):
        if datos_evento['nota'] == self.siguiente_nota:
            try:
                self.siguiente_nota = self.partitura.siguiente()[1]
            except StopIteration:
                self.ultima_nota = True
            if self.ultima_nota:
                termine_de_evaluar.emitir(estuvo_bien=True)
                tecla_pulsada.desconectar_por_id('evaluando')
        else:
            termine_de_evaluar.emitir(estuvo_bien=False)
            tecla_pulsada.desconectar_por_id('evaluando')
