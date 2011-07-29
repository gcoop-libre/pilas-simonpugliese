import pilas

class Osvaldo(pilas.actores.Actor):

    def __init__(self, x=0, y=0):
        pilas.actores.Actor.__init__(self, "osvaldo.png")
        self.x = 100
        self.y = 100
        self.decir("A ver si me podes seguir...")
        self.escala = 0.5

