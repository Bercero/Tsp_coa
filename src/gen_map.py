#! /usr/bin/env python3.5
from random import random
from sys import argv
try:
    nc=int(argv[1])
    mapa=[0]
    for i in range(nc):
        random()
except:
    #TODO mejorar esta linea
    print('''USO:
    '''+argv[0]+''' num_ciudades agujeros simetrico
    ejemplo '''+argv[0]+''' 5 1 1
        crea un mapa de 5 ciudades no todas ellas directamente conectadas y con caminos simetricos''')
#lee parametros
#   tamaño , con o sin agujeros, simetrico o no
#generar nube de puntos (ciudades) en 2D
#unir ciudades
#    o todas con todas
#        simetricamente o asimetricamente(la distancia real * factor aleatorio pequeño
#  o conectar con las mas cercana (un cierto radio) (comprobar despues la conexion total del grafo)
#guardar en fichero con nombre indicando tamaño y tipo + num secuencia

