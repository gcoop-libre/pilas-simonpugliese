import pilas

class Tecla(pilas.actores.Actor):
    
    def __init__(self, tipo_de_tecla, nota, x, y):
        imagen = "data/" + tipo_de_tecla + ".png"
        self.nota = nota
        pilas.actores.Actor.__init__(self, imagen, x=x, y=y)
        self.definir_centro(("centro", "arriba"))
        self._cargar_sonido(nota, pilas)
        if tipo_de_tecla == 'blanca':
            self.z = 100
        
    def pulsar(self):
        try:
            self.sonido.reproducir()
        except:
            pass
        self.escala = 0.95
        self.escala = [1], 0.5

    def _cargar_sonido(self, numero_nota, pilas):
        notas = {
            3: 'c.wav',
        }
        try:
            self.sonido = pilas.sonidos.cargar(notas[numero_nota])
        except:
            pass
