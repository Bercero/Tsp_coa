#! /usr/bin/env python3.5
from gen_map import Mapa
from config import get_args, init_config
from pickle import load
from random import random

class tsp_as:
    def __init__(self, mapa, max_it, max_it_sc, nh, algoritmo, np, alfa, beta, p_evap, fac_elitismo=1):
        self.mapa = mapa
        self.nc = mapa.get_num_ciudades()
        self.max_it = max_it
        self.max_it_sc = max_it_sc
        self.nh = nh
        self.alfa = alfa
        self.beta = beta
        self.p_evap = p_evap
        self.m_feromonas = [[1 for x in range(self.nc)] for i in range(self.nc)]
        self.fac_elitismo = fac_elitismo
        if algoritmo == 'AS':
            self.actualizar_feromonas = self.actualizar_feromonas_as
        elif algoritmo == 'AS_ELITISTA':
            self.actualizar_feromonas = self.actualizar_feromonas_as_elitista

        self.mejor_ruta=None
        self.init_result(algoritmo)
        self.np = np  # TODO

    def ejecutar(self):
        self.actualizar_g()
        # self.mejor_ruta=None
        for it in range(self.max_it):
            rutas = []
            for h in range(self.nh):
                rutas.append(self.lanzar_hormiga())
            self.actualizar_feromonas(rutas)

            if self.convergencia():
                break
        self.resultados['it']=it
        self.resultados['distancia']=self.mejor_dist
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

    def actualizar_feromonas_as(self, rutas):
        self.evaporar_feromonas()
        max_calidad = 0
        mejor_ruta = None
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
        mejor_ruta = None
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
            s += self.mapa.get_dist_norm(i, (i + 1) % self.nc)
        return 1 / s

    def init_result(self,algoritmo):
        self.resultados={'id':self.mapa.get_id()}
        if self.mapa.get_agujeros():
            self.resultados['agujeros']=True
        else :
            self.resultados['agujeros']=False
        if self.mapa.get_simetrico():
            self.resultados['simetrico']=True
        else :
            self.resultados['simetrico']=False
        self.resultados['nc']=self.nc
        self.resultados['nh']=self.nh
        self.resultados['alfa']=self.alfa
        self.resultados['beta']=self.beta
        self.resultados['p_evap']=self.p_evap
        self.resultados['algoritmo']=algoritmo
        if algoritmo == 'AS_ELITISTA':
            self.resultados['factor_elitismo']=self.fac_elitismo

    def guardar_result(self):
        with open('resultados.dat', 'w') as f:
            keys=self.resultados.keys()
            for k in keys:
                f.write(k+'='+str(self.resultados[k])+',')




if __name__ == '__main__':
    try :
        args=get_args()
    except:
        init_config()
        print('se ha generado un archivo de configuración de ejemplo')
        exit()
    with open(args['mapa'], 'rb') as f:
        mapa = load(f)
        max_it=int(args['max_it'])
        max_it_sc=int(args['max_it_sc'])
        nh=int(args['nh'])
        algoritmo=args['algoritmo']
        np=int(args['np'])
        alfa=float(args['alfa'])
        beta=float(args['beta'])
        p_evap=float(args['p_evap'])
        factor_elitismo=float(args['factor_elitismo'])
    t = tsp_as(mapa, max_it, max_it_sc, nh, algoritmo, np, alfa, beta, p_evap, factor_elitismo)
    t.ejecutar()

#
#       mapa(de cualquier tipo) mismo tratamiento?????
#    bucle mientras no fin
#       lanzar hormigas paralelas
#       esperar hormigas
#       actualizar fermonas segun algoritmo
#    escribir resultados en pantalla y en fichero
# paralelismo
