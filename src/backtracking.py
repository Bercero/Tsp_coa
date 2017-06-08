#! /usr/bin/env python3.5
from mapas import Mapa
from sys import argv
from pickle import load


class BackTracking:
    def __init__(self, mapa):
        self.mapa = mapa
        self.mejores_rutas = []
        self.mejor_distancia = 0
        self.nc = self.mapa.get_num_ciudades()

    def ejecutar(self):
        ruta = [0]
        candidatas = [c for c in range(1, self.nc)]
        self.back(ruta, candidatas)
        return self.mejores_rutas, self.mejor_distancia

    def back(self, ruta, candidatas):
        if len(candidatas):
            for c in candidatas:
                ruta_aux = ruta[:]
                candidatas_aux = candidatas[:]
                ruta_aux.append(c)
                candidatas_aux.remove(c)
                self.back(ruta_aux, candidatas_aux)
        else:
            self.actualizar_mejor(ruta)

    def actualizar_mejor(self, ruta):
        distancia = 0.0
        for i in range(self.nc):
            distancia += self.mapa.get_dist(ruta[i], ruta[(i + 1) % self.nc])

        if len(self.mejores_rutas):
            if distancia == self.mejor_distancia:
                self.mejores_rutas.append(ruta)
            elif distancia < self.mejor_distancia:
                self.mejores_rutas = [ruta]
                self.mejor_distancia = distancia
        else:
            self.mejores_rutas = [ruta]
            self.mejor_distancia = distancia

if __name__ == '__main__':
    with open(argv[1], 'rb') as f:
        mapa = load(f)

    rutas, distancia = BackTracking(mapa).ejecutar()
    print('las rutas mas cortas para el mapa con id {0} con distancia {1}'.format(mapa.id, distancia))
    for r in rutas:
        print(r)
