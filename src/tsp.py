#! /usr/bin/env python3.5
from gen_map import Mapa
from pickle import load
from random import random


class tsp_as:
    def __init__(self, mapa):
        self.mapa = mapa
        self.nc = mapa.get_num_ciudades()
        self.m_feromonas = [[1 for x in range(self.nc)] for i in range(self.nc)]

    def ejecutar(self, max_it, nh, algoritmo, np, alfa, beta):
        self.alfa=alfa
        self.beta=beta
        self.actualizar_g()
        for it in range(max_it):
            rutas = []
            for h in range(nh):
                rutas.append(self.soltar_hormiga())
            self.actualizar_feromonas(rutas)
            if self.convergencia():
                break

    def soltar_hormiga(self):
        # se parte siempre de la primera ciudad
        ruta = [0]
        for i in range(1, self.nc):
            elecciones = self.get_probobabilidades(ruta)
            r = random()
            p_acum = 0.0
            elegida = None
            for e in elecciones:
                p_acum += e['p']
                if r < p_acum:
                    elegida = e['id']
                    break
            ruta.append(elegida)
        return ruta

    def actualizar_feromonas(self, rutas):
        self.evaporar_feromonas()



        self.actualizar_g()

    def evaporar_feromonas(self):
        for origen in self.m_feromonas:
            for destino in range(len(origen)):
                origen[destino] -= 1
                if origen[destino] < 1:
                    origen[destino]=1

    def convergencia(self):

        return False

    def get_probobabilidades(self, ruta):
        i = ruta[-1]
        sumatorio_gi = 0.0
        candidatas = []
        for j in range(len(self.g[i])):
            if j not in ruta:
                sumatorio_gi += self.g[i][j]
                candidatas.append(j)
        probabilidades = []
        for j in candidatas:
            p = self.g[i][j] / sumatorio_gi
            probabilidades.append({'id': j, 'p': p})
        return probabilidades

    def actualizar_g(self):
        self.g=[[None]*self.nc for i in range(self.nc)]
        for i in range(self.nc):
            for j in range(self.nc):
                if i != j:
                    f_ij = self.m_feromonas[i][j]*self.alfa
                    h_ij = self.mapa.get_distancia(i, j)*self.beta
                    self.g[i][j] = f_ij/h_ij

if __name__ == '__main__':
    # TODO
    fichero = "mapas/mapa.mp"
    max_it = 1
    nh = 5
    algoritmo = 0
    np = 1
    alfa=1
    beta=1
    with open(fichero, 'rb') as f:
        mapa = load(f)
    t = tsp_as(mapa)
    t.ejecutar(max_it, nh, algoritmo, np, alfa, beta)

# main
#   leer parametros de configuracion
#       mapa(de cualquier tipo) mismo tratamiento?????
#       numero de hormigas
#       tipo de algoritmo
#    bucle mientras no fin
#       lanzar hormigas paralelas
#       esperar hormigas
#       actualizar fermonas segun algoritmo 
#       fin si max iterciones o convergencia
#        otras condiciones posibles serian el tiempo de proceso y acercarse a una solucion optima conocida, pero no los voy a aplicar
#    escribir resultados en pantalla y en fichero
# paralelismo
