import pilas
import piano
from interprete import Interprete
import partitura

from pilas.actores import Animado


pilas.iniciar(titulo='Simon pugliese')



pilas.avisar('Usa alt+q para salir.')
pilas.fondos.Pasto()
b = piano.PianoNuevo(-300, 200)
p = partitura.Partitura('partituras/la_yumba.csv')
interprete = Interprete(p)

pilas.ejecutar()


