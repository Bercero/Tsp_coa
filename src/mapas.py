#! /usr/bin/env python3.5
from random import random, randint
from math import hypot
from pickle import dump
from os import makedirs, listdir

class Mapa:
    def __init__(self, nc):
        self.escala = 1000  # ancho y largo del mapa en kilometros
        self.id = 0
        # lista de nc ciudades con cordenadas aleatorias
        self.cords = [{} for i in range(nc)]
        for i in range(nc):
            self.cords[i]['x'] = int(random() * self.escala)
            self.cords[i]['y'] = int(random() * self.escala)

        # calculo de la matriz de distacias
        self.m_dist = [[0] * nc for i in range(nc)]
        max_dist = 0
        for i in range(nc):
            for j in range(i + 1, nc):
                x = self.cords[i]['x'] - self.cords[j]['x']
                y = self.cords[i]['y'] - self.cords[j]['y']
                distancia = hypot(x, y)
                self.m_dist[i][j] = distancia
                self.m_dist[j][i] = distancia
                if distancia > max_dist:#TODO max distancia tal vez deveria tener otro valor(multiplicar por el numero de ciudades?)
                    max_dist = distancia
        self.m_dist_norm = [[0] * nc for i in range(nc)]
        for i in range(nc):
            for j in range(nc):
                self.m_dist_norm[i][j]=self.m_dist[i][j]/max_dist
        # almacenamiento del objeto en un archivo para su uso posterior
        self.guardar()

    def guardar(self):
        directory = 'mapas/{0}/'.format(self.get_num_ciudades())
        makedirs(directory, mode=0o775, exist_ok=True)

        self.id = self.get_num_ciudades()*100 + len(listdir(directory))
        name = directory + '/mapa{0}_{1}.mp'.format(self.get_num_ciudades(), len(listdir(directory)))
        with open(name, 'wb') as f:
            dump(self, f)

    def get_dist(self, a, b):
        return self.m_dist[a][b]

    def get_dist_norm(self, a, b):
        return self.m_dist_norm[a][b]

    def pib(self):
        for i in self.cords:
            print(i)
        for i in self.m_dist:
            print(i)
        for i in self.m_dist_norm:
            print(i)

    def get_num_ciudades(self):
        return len(self.cords)

    def get_id(self):
        return self.id

if __name__ == '__main__':
    from sys import argv

    nc = int(argv[1])
    m = Mapa(nc)
