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
        self.sonido.reproducir()

    def _cargar_sonido(self, nota, pilas):
        self.sonido = pilas.sonidos.cargar('c.wav')
        afinacion = 2 ** (nota / 12.0) #para no importar math
        self.sonido.definir_pitch(afinacion)

