import csv


NOTAS = { 'C':1, 'C#':2, 'D':3, 'D#':4, 'E':5,'F':6,
          'F#':7, 'G':8, 'G#':9, 'A':10, 'A#':11, 'B':12 }

class Partitura:

    def __init__(self, nombre_archivo):
        self.leer_desde_csv(nombre_archivo)

    def leer_desde_csv(self, nombre_archivo):
        '''
        Recibe la ruta del archivo CSV donde se encuentra la partitura
        '''
        archivo = open(nombre_archivo, 'r')
        lector_csv = csv.reader(archivo)
        self.notas = [(int(figura), NOTAS[nota] + 12 * (int(octava)-1)) for
                      figura, nota, octava in lector_csv]



if __name__ == '__main__':
    p = Partitura('partituras/la_yumba.csv')
    print p.notas
