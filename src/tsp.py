#! /usr/bin/env python3.5
from gen_map import Mapa
from pickle import load


class tsp_coa:
    def __init__(self, mapa):
        self.mapa = mapa
        nc = mapa.get_num_ciudades()
        self.m_feromonas = [[0 for x in range(nc)] for i in range(nc)]

    def ejecutar(self, max_it, nh, algoritmo, np):
        for it in range(max_it):
            rutas = []
            for h in range(nh):
                rutas.append(self.soltar_hormiga())
            self.actualizar_feromonas(rutas)
            self.evaporar_feromonas()
            if self.convergencia():
                break

    def soltar_hormiga(self):
        # se parte siempre de la primera ciudad
        actual = 0
        ruta = [actual]
        nc = self.mapa.get_num_ciudades()
        candidatas = list(range(1, nc))
        for i in range(1, nc):
            elegida = candidatas[0]
            min_dist = self.mapa.get_distancia(actual, elegida)
            for c in candidatas:
                m = self.mapa.get_distancia(actual, c)
                if min_dist > m:
                    min_dist = m
                    elegida = c
            ruta.append(elegida)
            candidatas.remove(elegida)
        return ruta

    def actualizar_feromonas(self, rutas):
        nc = self.mapa.get_num_ciudades()
        for r in rutas:
            for i in range(nc):
                origen = r[i]
                destino = r[(i + 1) % nc]
                self.m_feromonas[origen][destino] += 1

    def evaporar_feromonas(self):
        for origen in self.m_feromonas:
            for destino in range(len(origen)):
                if origen[destino] != 0:
                    origen[destino] -= 1

    def convergencia(self):

        return False


if __name__ == '__main__':
    # TODO
    fichero = "mapas/mapa.mp"
    max_it = 1
    nh = 5
    algoritmo = 0
    np = 1

    with open(fichero, 'rb') as f:
        mapa = load(f)
    t = tsp_coa(mapa)
    t.ejecutar(max_it, nh, algoritmo, np)

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
