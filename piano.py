import tecla
import pilas

class PianoNuevo:
    
    def __init__(self, dx, dy):
        pilas.eventos.click_de_mouse.connect(self.cuando_hace_click)
        self._crear_teclas(dx, dy)

    def _crear_teclas(self, dx, dy):
        ancho = 37
        contador = 0
        negras = [1, 3, 6, 8, 10]
        for nota in xrange(12, 36):
            if nota%12 in negras:
                color = 'negra'
                posicion_x = dx + (ancho * (contador) - ancho/2)
            else:
                color = 'blanca'
                posicion_x = dx + (ancho * contador)
                contador += 1
            
            tecla.Tecla(color, nota, posicion_x, dy)


            


                          
    def cuando_hace_click(self, evento):
        tecla = pilas.actores.utils.obtener_actor_en(evento.x, evento.y)

        if tecla and hasattr(tecla, 'pulsar'):
            tecla.pulsar()

        

