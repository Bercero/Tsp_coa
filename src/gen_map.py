#! /usr/bin/env python3.5
from random import random
from math import hypot
from pickle import dump
from os import walk
class mapa:
    def __init__(self,nc):
        self.escala=1000 #ancho y largo del mapa en kilometros
        self.agujeros=False #TODO
        self.simetrico=True #TODO
                
        #lista de nc ciudades con cordenadas aleatorias
        self.cords=[{'x':None,'y':None} for i in range(nc)]
        for i in range(nc):
            self.cords[i]['x']=int(random()*self.escala)
            self.cords[i]['y']=int(random()*self.escala)
            
        #calculo de la matriz de distacias
        #TODO solo el tipo simple
        self.dist=[[0]*nc for i in range(nc)]
        for i in range(nc):
            for j in range(i+1,nc):
                x=self.cords[i]['x']-self.cords[j]['x']
                y=self.cords[i]['y']-self.cords[j]['y']
                self.dist[i][j]=hypot(x,y)
                self.dist[j][i]=self.dist[i][j]     
        #almacenamiento del objeto en un archivo para su uso posterior
        self.guardar()
    def guardar(self):
        #TODO pasar variable de entorno para encontrar la carpeta mapas
        #TODO guardar como mapas/n_ciudades/simetrico_agujeros_1.mp
        prefix='mapas/'
        fichero=prefix+'mapa.mp'

        ficheros = []
        for (path, dirs, files) in walk(prefix):
             ficheros.extend(files)
             break
        print(ficheros)
        with open(fichero,'wb') as f:
             dump(self,f)
    #TODO cambiar nombre por __print__ o algo asi
    def pib(self):
        for i in self.cords:
            print(i)
        for i in self.dist:
            print(i)     
if __name__ == '__main__':
    from sys import argv
#try:
    #el primer argumento es el numero de ciudades
    nc=int(argv[1])
    m=mapa(nc)
    m.pib()
    
#except:
    #TODO mejorar esta linea y devolver error
    print('''USO:
    '''+argv[0]+''' num_ciudades agujeros simetrico
    ejemplo '''+argv[0]+''' 5 1 1
        crea un mapa de 5 ciudades no todas ellas directamente conectadas y con caminos simetricos''')
    
#lee parametros
#   tamaño , con o sin agujeros, simetrico o no
#unir ciudades
#    o todas con todas
#        simetricamente o asimetricamente(la distancia real * factor aleatorio pequeño
#  o conectar con las mas cercana (un cierto radio) (comprobar despues la conexion total del grafo)
#guardar en fichero con nombre indicando tamaño y tipo + num secuencia
# getters: distancia entre dos ciudades, numero de ciudades

