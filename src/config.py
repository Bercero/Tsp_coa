#! /usr/bin/env python3.5
fichero='config'
def init_config():
    with open(fichero, 'w') as f:
        f.write("""#ejemplo de configuracion
#requiere que se haya creado antes con el comando gen_map.py (el unico parametro es el numero de ciudades)
mapa=mapas/mapa.mp
max_it=1000
#maximo numero de iteraciones sin mejorar la solucion
max_it_sc=25
nh=50
#elegir entre uno de estos algoritmos
#algoritmo=AS
algoritmo=AS_ELITISTA
#algoritmo=AS_RANK_BASED
#el peso de las feromonas aumenta con alfa
#el peso de las distancias mas pequeñas aumenta con beta
#pueden tomar cualquier valor positivo pero yo uso valores que sumen 1
alfa=0.5
beta=0.5
p_evap=0.25
#solo para el elitista
factor_elitismo=1
#solo para el basado en ranking
#r y w tienen que ser enteros y w mayor que r
r=10
w=10""")
def get_args():
    with open(fichero, 'r') as f:
        lineas = f.readlines()
        lineas_sin_espacios=[]
        for l in lineas:
            if l[0] != '#':
                lineas_sin_espacios.append(l.split())
        pares=[]
        for l in lineas_sin_espacios:
            for sub_l in l:
                pares.append(sub_l.split('='))
        args={}
        for p in pares:
            args[p[0]]=p[1]
    return args