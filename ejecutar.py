import pilas
import piano
from interprete import Interprete
import partitura

from pilas.actores import Animado


pilas.iniciar(usar_motor='qt', titulo='Simon pugliese')


pilas.fondos.Pasto()
b = piano.PianoNuevo(-240, -75)
p = partitura.Partitura('partituras/la_yumba.csv')
interprete = Interprete(p, b)

pilas.ejecutar()


