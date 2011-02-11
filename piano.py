import tecla
import pilas

class PianoNuevo:
    
    def __init__(self, dx, dy):
        pilas.eventos.click_de_mouse.connect(self.cuando_hace_click)
        self._crear_teclas(dx, dy)

    def _crear_teclas(self, dx, dy):
        ancho = 37
        
        tecla.Tecla('blanca', 12, dx + ancho * 0,  dy)
        tecla.Tecla('negra', 13, dx + ancho * 1 - ancho/2,  dy)
        tecla.Tecla('blanca', 14, dx + ancho * 1,  dy)
        tecla.Tecla('negra', 15, dx + ancho/2 * 3,  dy)
        tecla.Tecla('blanca', 16, dx + ancho * 2,  dy)
        tecla.Tecla('blanca', 17, dx + ancho * 3,  dy)
        tecla.Tecla('negra', 18, dx + ancho/2 * 7,  dy)   
        tecla.Tecla('blanca', 19, dx + ancho * 4,  dy)
        tecla.Tecla('negra', 20, dx + ancho/2 * 9,  dy)
        tecla.Tecla('blanca', 21, dx + ancho * 5,  dy)
        tecla.Tecla('negra', 22, dx + ancho/2 * 11,  dy)        
        tecla.Tecla('blanca', 23, dx + ancho * 6,  dy)
       
                          
    def cuando_hace_click(self, evento):
        tecla = pilas.actores.utils.obtener_actor_en(evento.x, evento.y)

        if tecla and hasattr(tecla, 'pulsar'):
            tecla.pulsar()

        

