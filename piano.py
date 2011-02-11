import tecla

class PianoNuevo:
    def __init__(self, dx, dy):
        tecla.Tecla('blanca', dx + 0,   dy)
        tecla.Tecla('blanca', dx + 50,  dy)
        tecla.Tecla('blanca', dx + 100, dy)
        tecla.Tecla('blanca', dx + 150, dy)
        tecla.Tecla('blanca', dx + 200, dy)
        tecla.Tecla('blanca', dx + 250, dy)
        tecla.Tecla('blanca', dx + 300, dy)
        
        tecla.Tecla('negra', dx + 25, dy)
        tecla.Tecla('negra', dx + 75, dy)
        
        tecla.Tecla('negra', dx + 225 - 50, dy)        
        tecla.Tecla('negra', dx + 225, dy)
        tecla.Tecla('negra', dx + 275, dy)