import numpy as np
import matplotlib.pyplot as plt


class Estadisticas:
    def __init__(self):
        with open('resultados.dat', 'r') as f:
            lineas = f.readlines()

        self.resultados = []
        for l in lineas:
            if(l[0]!='#'):
                elements = l.split(',')
                variables = {}
                for e in elements:
                    variables[e.split('=')[0]] = e.split('=')[1]
                self.resultados.append(variables)

        plt.rcdefaults()

    def resultadosPorMapa(self):
        s = sorted(self.resultados, key=lambda r: r['id'])
        listas_ids = {}
        while len(s) != 0:
            r = s.pop(0)
            if r['id'] in listas_ids.keys():
                listas_ids[r['id']].append(r)
            else :
                listas_ids[r['id']] = [r]

        j = 0
        for lol in listas_ids.items():
            algoritmos = [r['algoritmo'] for r in lol[1]]
            iteraciones = [int(r['it']) for r in lol[1]]
            distancias = [float(r['distancia']) for r in lol[1]]

            max_distancia = 0
            for d in distancias:
                if d > max_distancia:
                    max_distancia = d

            plt.figure(j)
            j += 1
            plt.subplot(211)
            ax = plt.gca()

            y_pos = np.arange(len(algoritmos))

            ax.barh(y_pos, iteraciones, align='center', color='green')
            ax.set_yticks(y_pos)
            ax.set_yticklabels(algoritmos)
            ax.set_xlabel('iteraciones')
            ax.set_title('iteraciones del mapa {0}'.format(lol[0]))

            plt.subplot(212)
            ax = plt.gca()
            y_pos = np.arange(len(algoritmos))
            ax.set_yticks(y_pos)
            ax.set_yticklabels(algoritmos)
            ax.set_xlabel('distacia')
            ax.set_autoscalex_on(False)
            ax.set_xbound(0, max_distancia+ 0.1*max_distancia)
            ax.set_title('distancia de la ruta hallada para el mapa {0}'.format(lol[0]))
            plt.plot(distancias, y_pos, 'bo')
        plt.show()

    def resultadosPorAlgoritmo(self):
        s = sorted(self.resultados, key=lambda r: r['algoritmo'])
        listas_algoritmos = {}
        while len(s) != 0:
            r = s.pop(0)
            if r['algoritmo'] in listas_algoritmos.keys():
                listas_algoritmos[r['algoritmo']].append(r)
            else:
                listas_algoritmos[r['algoritmo']] = [r]
        j = 0
        for lol in listas_algoritmos.items():
            nc = [int(r['nc']) for r in lol[1]]
            iteraciones = [int(r['it']) for r in lol[1]]
            distancias = [float(r['distancia']) for r in lol[1]]

            plt.figure(j)
            j += 1
            plt.subplot(211)
            ax = plt.gca()
            ax.set_yticks(nc)
            ax.set_yticklabels(nc)
            ax.set_xlabel('iteraciones')
            ax.set_ylabel('numero de ciudades')
            ax.set_title('iteraciones para el algoritmo {0}'.format(lol[0]))
            # ax.set_autoscalex_on(False)
            # ax.set_xbound(0, 1000)
            plt.plot(iteraciones, nc, 'g.')

            plt.subplot(212)
            ax = plt.gca()
            ax.set_yticks(nc)
            ax.set_yticklabels(nc)
            ax.set_xlabel('distancia')
            ax.set_ylabel('numero de ciudades')
            ax.set_title('distancia para el algoritmo {0}'.format(lol[0]))
            plt.plot(distancias, nc, 'g.')

        plt.show()

    def resultadosPorAlpha(self):
        s = sorted(self.resultados, key=lambda r: r['id'])
        listas_ids = {}
        while len(s) != 0:
            r = s.pop(0)
            if r['id'] in listas_ids.keys():
                listas_ids[r['id']].append(r)
            else:
                listas_ids[r['id']] = [r]

        j = 0
        for lol in listas_ids.items():
            alfa = [float(r['alfa']) for r in lol[1]]
            beta = [float(r['beta']) for r in lol[1]]
            iteraciones = [int(r['it']) for r in lol[1]]
            distancias = [float(r['distancia']) for r in lol[1]]

            plt.figure(j)
            j += 1
            plt.subplot(211)
            ax = plt.gca()
            ax.set_yticks(alfa)
            ax.set_yticklabels(alfa)
            ax.set_xlabel('iteraciones')
            ax.set_ylabel('alfa y beta')
            ax.set_title('iteraciones para disitintos niveles de alfa(verde) y beta(rojo), mapa {0}'.format(lol[0]))
            # ax.set_autoscalex_on(False)
            # ax.set_xbound(0, 1000)
            plt.plot(iteraciones, alfa, 'g.')
            plt.plot(iteraciones, beta, 'r.')

            plt.subplot(212)
            ax = plt.gca()
            ax.set_yticks(alfa)
            ax.set_yticklabels(alfa)
            ax.set_xlabel('distancia')
            ax.set_ylabel('alfa y beta')
            ax.set_title('distancias para disitintos niveles de alfa(verde) y beta(rojo), mapa {0}'.format(lol[0]))

            # ax.set_autoscalex_on(False)
            # ax.set_xbound(0, 1000)
            plt.plot(distancias, alfa, 'g.')
            plt.plot(distancias, beta, 'r.')

        plt.show()

if __name__ == '__main__':
    e = Estadisticas()
    # e.resultadosPorMapa()
    # e.resultadosPorAlgoritmo()
    e.resultadosPorAlpha()


