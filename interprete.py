import pilas

BPM = 180.0

    
class Interprete:
    
    def __init__(self, partitura, piano):
        self.partitura = partitura
        self.piano = piano
        pilas.mundo.tasks.agregar(60 / BPM / 4.0, self.procesar_tick, ())
        self.ticks_que_faltan_a_la_siguiente_nota = 0
        
    def procesar_tick(self):
        if self.ticks_que_faltan_a_la_siguiente_nota <= 0:
            self._ejecutar_nota()
        else:
            self.ticks_que_faltan_a_la_siguiente_nota -= 1
        return True
    
    def _ejecutar_nota(self):
        (duracion, nota) = self.partitura.siguiente()
        self.ticks_que_faltan_a_la_siguiente_nota = 64.0 / duracion
        self.piano.reproducir_nota(nota)
