#! /usr/bin/env python3.5
from random import random, randint
from math import hypot
from pickle import dump
from os import walk


class Mapa:
    def __init__(self, nc):
        self.id=str(nc)+'-'+str(randint(0,1000))
        self.escala = 1000  # ancho y largo del mapa en kilometros
        self.agujeros = False  # TODO
        self.simetrico = True  # TODO

        # lista de nc ciudades con cordenadas aleatorias
        self.cords = [{'x': None, 'y': None} for i in range(nc)]
        for i in range(nc):
            self.cords[i]['x'] = int(random() * self.escala)
            self.cords[i]['y'] = int(random() * self.escala)

        # calculo de la matriz de distacias
        # TODO solo el tipo simple
        self.m_dist = [[0] * nc for i in range(nc)]
        max_dist=0
        for i in range(nc):
            for j in range(i + 1, nc):
                x = self.cords[i]['x'] - self.cords[j]['x']
                y = self.cords[i]['y'] - self.cords[j]['y']
                distancia=hypot(x, y)
                self.m_dist[i][j] = distancia
                self.m_dist[j][i] = distancia
                if distancia > max_dist:
                    max_dist=distancia
        self.m_dist_norm = [[0] * nc for i in range(nc)]
        for i in range(nc):
            for j in range(nc):
                self.m_dist_norm[i][j]=self.m_dist[i][j]/max_dist
        # almacenamiento del objeto en un archivo para su uso posterior
        self.guardar()

    def guardar(self):
        # TODO pasar variable de entorno para encontrar la carpeta mapas
        # TODO guardar como mapas/n_ciudades/simetrico_agujeros_1.mp
        prefix = 'mapas/'
        fichero = prefix + 'mapa.mp'

        ficheros = []
        for (path, dirs, files) in walk(prefix):
            ficheros.extend(files)
            break
        print(ficheros)
        with open(fichero, 'wb') as f:
            dump(self, f)

    def get_dist(self, a, b):
        return self.m_dist[a][b]

    def get_dist_norm(self, a, b):
        return self.m_dist_norm[a][b]
    # TODO cambiar nombre por __print__ o algo asi
    def pib(self):
        for i in self.cords:
            print(i)
        for i in self.m_dist:
            print(i)
        for i in self.m_dist_norm:
            print(i)

    def get_num_ciudades(self):
        return len(self.cords)

    def get_agujeros(self):
        return self.agujeros

    def get_simetrico(self):
        return self.simetrico
    def get_id(self):
        return self.id

if __name__ == '__main__':
    from sys import argv

    try:
    # el primer argumento es el numero de ciudades
        nc = int(argv[1])
        m = Mapa(nc)
        m.pib()

    except:
        # TODO mejorar esta linea y devolver error
        print('''USO:
        ''' + argv[0] + ''' num_ciudades agujeros simetrico
        ejemplo ''' + argv[0] + ''' 5 1 1
        crea un mapa de 5 ciudades no todas ellas directamente conectadas y con caminos simetricos''')

