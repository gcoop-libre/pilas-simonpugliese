import pilas
from interprete import Interprete, termine_de_tocar
from tecla import tecla_pulsada

termine_de_evaluar = pilas.evento.Evento("Evaluacion terminada")

class Osvaldo(pilas.actores.Actor):

    def __init__(self, partitura, piano, x=0, y=0):
        self.espera = 1
        pilas.actores.Actor.__init__(self, "img/osvaldo.png")
        self.x = 120
        self.y = 100
        self.decir("A ver si me podes seguir...", True, False)
        self.partitura = partitura
        self.piano = piano

    def interpretar(self):
        def comenzar_a_tocar():
            self.interprete = Interprete(self.partitura, self.piano)
            termine_de_tocar.conectar(self.evaluar, 'interpretando')
        pilas.escena_actual().tareas.una_vez(self.espera, comenzar_a_tocar)

    def evaluar(self, datos_evento):
        def  ahora_te_toca_a_ti():
            self.decir("Ahora te toca ti...", True, False)
            self.partitura.reiniciar()
            self.siguiente_nota = self.partitura.siguiente()[1]
            self.ultima_nota = False
            termine_de_tocar.desconectar_por_id('interpretando')
            tecla_pulsada.conectar(self.evaluar_tecla, 'evaluando')

        pilas.escena_actual().tareas.una_vez(self.espera, ahora_te_toca_a_ti)

    def evaluar_tecla(self, datos_evento):
        def informar_ok():
            termine_de_evaluar.emitir(estuvo_bien=True)
            tecla_pulsada.desconectar_por_id('evaluando')

        def informar_error():
            termine_de_evaluar.emitir(estuvo_bien=False)
            tecla_pulsada.desconectar_por_id('evaluando')

        if datos_evento['nota'] == self.siguiente_nota:
            try:
                self.siguiente_nota = self.partitura.siguiente()[1]
            except StopIteration:
                self.ultima_nota = True
            if self.ultima_nota:
                pilas.escena_actual().tareas.una_vez(self.espera, informar_ok)
        else:
            pilas.escena_actual().tareas.una_vez(self.espera, informar_error)
