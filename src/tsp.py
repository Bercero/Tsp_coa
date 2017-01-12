#! /usr/bin/env python3.5
#TODO arreglar el tema del paquete (__init__.py)
from gen_map import Mapa
from pickle import load
class tsp_coa:
    
    def __init__(self,mapa):
        self.mapa=mapa
        nc=mapa.get_num_ciudades()
        self.m_feromonas=[[0 for x in range(nc)]for i in range(nc)]
        
    def ejecutar(self, max_it, nh, algoritmo,np):
        for it in range(max_it):
            caminos=[]
            for h in range(nh):
                caminos.append(self.soltar_hormiga())
            self.actualizar_feromonas(caminos)
            self.evaporar_feromonas(caminos)
            if self.convergencia():
                break
    def soltar_hormiga(self):
        #se parte siempre de la primera ciudad
        camino=[0]
        min=0
        nc=self.mapa.get_num_ciudades()
        #for i in range(nc):
             
        self.mapa.pib()
        
            
    def actualizar_feromonas(self,a):
        print(a)
    def evaporar_feromonas(self,a):
        print(a)
    def convergencia(self):
        return True
if __name__ == '__main__':
    #TODO
    fichero="mapas/mapa.mp"
    max_it=1
    nh=5
    algoritmo=0
    np=1
    
    with open(fichero,'rb') as f:
        mapa=load(f)
    
    t=tsp_coa(mapa)
    t.ejecutar(max_it,nh,algoritmo,np)

#main
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
