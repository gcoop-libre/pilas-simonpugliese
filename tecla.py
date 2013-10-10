import pilas

tecla_pulsada = pilas.evento.Evento("Nota pulsada")

class Tecla(pilas.actores.Actor):

    def __init__(self, tipo_de_tecla, nota, x, y):
        imagen = "data/" + tipo_de_tecla + ".png"
        self.nota = nota
        self.sonido = pilas.sonidos.cargar(nota + '.wav')
        pilas.actores.Actor.__init__(self, imagen, x=x, y=y)
        self.definir_centro(("centro", "arriba"))
        if tipo_de_tecla == 'blanca':
            self.z = 100

    def pulsar(self):
        try:
            self.sonido.reproducir()
        except:
            pass
        tecla_pulsada.emitir(nota=self.nota)
        self.escala = 0.95
        self.escala = [1], 0.5
