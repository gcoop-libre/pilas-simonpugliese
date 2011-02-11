import pilas
import piano
from interprete import Interprete

from pilas.actores import Animado


pilas.iniciar(titulo='Simon pugliese')



pilas.avisar('Usa alt+q para salir.')
pilas.fondos.Pasto()


b = piano.PianoNuevo(-200, 200)
interprete = Interprete()

pilas.ejecutar()


