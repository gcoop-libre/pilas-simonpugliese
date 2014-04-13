import csv


NOTAS = { 'C':0, 'C#':1, 'D':2, 'D#':3, 'E':4,'F':5,
          'F#':6, 'G':7, 'G#':8, 'A':9, 'A#':10, 'B':11 }

class Partitura:

    def __init__(self, nombre_archivo):
        self.leer_desde_csv(nombre_archivo)

    def leer_desde_csv(self, nombre_archivo):
        '''
        Recibe la ruta del archivo CSV donde se encuentra la partitura
        '''
        archivo = open(nombre_archivo, 'r')
        lector_csv = csv.reader(archivo)
        self._notas = [(int(figura), "%s%s" % (nota, octava)) for
                      figura, nota, octava in lector_csv]
        self.notas = iter(self._notas)
        self.largo = len(self._notas)

    def cortar_partitura(self, largo):
        if (largo > len(self._notas)):
            raise Exception()
        self.largo = largo
        self.notas = iter(self._notas[:largo])

    def reiniciar(self):
        self.notas = iter(self._notas[:self.largo])

    def siguiente(self):
        return self.notas.next()

if __name__ == '__main__':
    p = Partitura('partituras/la_yumba.csv')
    print list(p.notas)

    p.cortar_partitura(3)
    print list(p.notas)
