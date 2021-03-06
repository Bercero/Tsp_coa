#! /usr/bin/env python3.5
from mapas import Mapa
ALGORITMOS=['AS','AS_ELITISTA','AS_RANK_BASED']
from config import *
from pickle import load
from random import random, randint
class tsp_as:

    def __init__(self, mapa, max_it, max_it_sc, nh, nhl, algoritmo, alfa, beta, p_evap, fac_elitismo=1, r=0, w=0):
        self.mapa = mapa
        self.nc = mapa.get_num_ciudades()
        self.max_it = max_it
        self.max_it_sc = max_it_sc
        self.nh = nh
        self.nhl = nhl
        self.alfa = alfa
        self.beta = beta
        self.p_evap = p_evap
        self.m_feromonas = [[1 for x in range(self.nc)] for i in range(self.nc)]
        algoritmo = ALGORITMOS[algoritmo]
        if algoritmo == ALGORITMOS[0]:
            self.actualizar_feromonas = self.actualizar_feromonas_as
        elif algoritmo == ALGORITMOS[1]:
            self.fac_elitismo = fac_elitismo
            self.actualizar_feromonas = self.actualizar_feromonas_as_elitista
        elif algoritmo == ALGORITMOS[2]:
            self.actualizar_feromonas = self.actualizar_feromonas_as_ranked
            self.convergencia= self.convergencia_ranking
            self.r_factor = r
            self.w_factor = w
            self.ranking = []
            self.covergencia = self.convergencia_ranking
        self.mejor_ruta=None
        self.init_result(algoritmo)

        self.mejor_dist = 0

        self.g = None

    def ejecutar(self):
        self.actualizar_g()
        for it in range(self.max_it):
            rutas = []
            for h in range(self.nh):
                rutas.append(self.lanzar_hormiga())
            for h in range(self.nhl):
                rutas.append(self.lanzar_hormiga_loca())
            self.actualizar_feromonas(rutas)

            if self.convergencia():
                break
        self.resultados['it'] = it
        self.resultados['distancia'] = self.mejor_dist
        self.guardar_result()

    def lanzar_hormiga(self):
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

    def lanzar_hormiga_loca(self):
        # se parte siempre de la primera ciudad
        ruta = [0]
        candidatas = [x for x in range(1, self.nc)]
        while len(candidatas) != 0:
            inaccesibles = []
            while len(candidatas) != 0:
                i = randint(0,len(candidatas)-1)
                if self.mapa.get_dist(ruta[-1], candidatas[i]) > 0:
                    ruta.append(candidatas.pop(i))
                    candidatas.extend(inaccesibles)
                    break
                else:
                    inaccesibles.append(candidatas.pop(i))
        # TODO controlar que es una ruta completa y en las hormigas normales tambien
        return ruta

    def actualizar_feromonas_as(self, rutas):
        self.evaporar_feromonas()
        max_calidad = 0
        for r in rutas:
            calidad = self.get_calidad(r)
            if calidad > max_calidad:
                max_calidad = calidad
                mejor_ruta = r
            for i in range(self.nc):
                self.m_feromonas[r[i]][r[(i + 1) % self.nc]] += calidad
        self.actualizar_mejor_ruta(mejor_ruta)
        self.actualizar_g()

    def actualizar_feromonas_as_elitista(self, rutas):
        self.evaporar_feromonas()
        max_calidad = 0
        for r in rutas:
            calidad = self.get_calidad(r)
            if calidad > max_calidad:
                max_calidad = calidad
                mejor_ruta = r
            for i in range(self.nc):
                self.m_feromonas[r[i]][r[(i + 1) % self.nc]] += calidad
        for i in range(self.nc):
            self.m_feromonas[mejor_ruta[i]][mejor_ruta[(i + 1) % self.nc]] += self.fac_elitismo * max_calidad
        self.actualizar_mejor_ruta(mejor_ruta)
        self.actualizar_g()

    def actualizar_feromonas_as_ranked(self, rutas):
        self.evaporar_feromonas()
        rutas.extend(self.ranking)
        rutas = sorted(rutas, key=self.get_calidad)
        rutas = self.ranking = rutas[:self.r_factor]

        for j in range(self.r_factor):
            ru = rutas[j]
            for i in range(self.nc):
                self.m_feromonas[ru[i]][ru[(i + 1) % self.nc]] += (self.w_factor - j) / (self.w_factor*4)
        ru = rutas[0]
        self.mejor_dist = 0
        for i in range(self.nc):
            self.mejor_dist += self.mapa.get_dist(ru[i], ru[(i + 1) % self.nc])
        self.mejor_ruta = ru
        self.actualizar_g()

    def actualizar_mejor_ruta(self, ruta):
        mejor_dist = 0
        for i in range(self.nc):
            mejor_dist += self.mapa.get_dist(ruta[i], ruta[(i + 1) % self.nc])

        if not self.mejor_ruta:
            self.mejor_ruta = ruta
            self.mejor_dist = mejor_dist
            self.it_sc = 0
        elif mejor_dist < self.mejor_dist:
            self.mejor_dist = mejor_dist
            self.mejor_ruta = ruta
            self.it_sc = 0

    def evaporar_feromonas(self):
        for i in range(self.nc):
            for j in range(self.nc):
                if i != j:
                    self.m_feromonas[i][j] *= (1 - self.p_evap)
                    if self.m_feromonas[i][j] < 1:
                        self.m_feromonas[i][j] = 1

    def convergencia(self):
        self.it_sc+=1
        return self.it_sc >= self.max_it_sc

    def convergencia_ranking(self):
        rutas_distintas=[]
        for r in self.ranking:
            if r not in rutas_distintas:
                rutas_distintas.append(r)
        n = len(rutas_distintas)/self.r_factor
        return n <= 0.50

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
        self.g = [[None] * self.nc for i in range(self.nc)]
        for i in range(self.nc):
            for j in range(self.nc):
                if i != j:
                    f_ij = self.m_feromonas[i][j] * self.alfa
                    h_ij = self.beta / self.mapa.get_dist_norm(i, j)
                    self.g[i][j] = f_ij * h_ij

    def get_calidad(self, ruta):
        s = 0
        for i in range(self.nc):
            s += self.mapa.get_dist_norm(ruta[i], ruta[(i + 1) % self.nc])
        return 1 / s

    def init_result(self, algoritmo):
        self.resultados={'id':self.mapa.get_id()}

        self.resultados['nc'] = self.nc
        self.resultados['nh'] = self.nh
        self.resultados['alfa'] = self.alfa
        self.resultados['beta'] = self.beta
        self.resultados['p_evap'] = self.p_evap
        self.resultados['algoritmo'] = algoritmo
        if algoritmo == 'AS_ELITISTA':
            self.resultados['factor_elitismo'] = self.fac_elitismo
        elif algoritmo =='AS_RANK_BASED':
            self.resultados['r'] = self.r_factor
            self.resultados['w'] = self.w_factor

    def guardar_result(self):
        with open('resultados.dat', 'a') as file:
            keys = sorted(self.resultados.keys())
            for k in keys[:-1]:
                file.write(k+'='+str(self.resultados[k])+',')
            file.write(keys[-1] + '=' + str(self.resultados[keys[-1]]) + '\n')

if __name__ == '__main__':
    try:
        args = get_args()
    except:
        init_config()
        print('se ha generado un archivo de configuración de ejemplo')
        exit()
    with open(args['mapa'], 'rb') as f:
        mapa = load(f)
    max_it = int(args['max_it'])
    max_it_sc = int(args['max_it_sc'])
    nh = int(args['nh'])
    nhl = int(args['nhl'])
    algoritmo=int(args['algoritmo'])
    alfa = float(args['alfa'])
    beta = float(args['beta'])
    p_evap = float(args['p_evap'])
    factor_elitismo = float(args['factor_elitismo'])
    r = int(args['r'])
    w = int(args['w'])
    t = tsp_as(mapa, max_it, max_it_sc, nh, nhl, algoritmo, alfa, beta, p_evap, factor_elitismo, r, w)
    t.ejecutar()
