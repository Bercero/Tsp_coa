#! /usr/bin/env python3.5
fichero='config'
def init_config():
    with open(fichero, 'w') as f:
        f.write("""#ejemplo de configuracion
mapa=mapas/mapa.mp
max_it=1000
max_it_sc=25
nh=5
algoritmo=AS_ELITISTA
np=1
alfa=0.5
beta=0.5
p_evap=0.25
factor_elitismo=1""")
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