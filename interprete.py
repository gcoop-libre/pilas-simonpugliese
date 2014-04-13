import pilas

BPM = 180.0


termine_de_tocar = pilas.evento.Evento("Termine de tocar")

class Interprete:

    def __init__(self, partitura, piano):
        self.partitura = partitura
        self.piano = piano
        pilas.mundo.agregar_tarea(60 / BPM / 4.0, self.procesar_tick)
        self.ticks_que_faltan_a_la_siguiente_nota = 0

    def procesar_tick(self):
        if self.ticks_que_faltan_a_la_siguiente_nota <= 0:
            try:
                self._ejecutar_nota()
            except StopIteration:
                termine_de_tocar.emitir()
                return False
        else:
            self.ticks_que_faltan_a_la_siguiente_nota -= 1

        return True

    def _ejecutar_nota(self):
        (duracion, nota) = self.partitura.siguiente()
        self.ticks_que_faltan_a_la_siguiente_nota = 64.0 / duracion
        self.piano.reproducir_nota(nota)
