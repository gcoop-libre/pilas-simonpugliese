import pilas
        

    
class Interprete:
    
    def __init__(self):
        pilas.mundo.tasks.agregar(0.10, self.procesar_tick, ())
        self.tick = 0
        
    def procesar_tick(self):
        self.tick += 1
        return True