import pilas

class Tecla(pilas.actores.Actor):
    def __init__(self, tipo_de_tecla, x, y):

        
        imagen = self._obtener_imagen(tipo_de_tecla)
        pilas.actores.Actor.__init__(self, imagen, x=x, y=y)
        self.definir_centro(("centro", "arriba"))
    
    def _obtener_imagen(self, tipo_de_tecla):
        imagenes = {
                    'negra': 'data/negra.png',
                    'blanca': 'data/blanca.png',
                    }
        return imagenes[tipo_de_tecla]