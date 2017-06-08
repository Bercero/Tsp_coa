import numpy as np
import matplotlib.pyplot as plt


class Estadisticas:
    def __init__(self):
        with open('resultados.dat', 'r') as f:
            lineas = f.readlines()

        self.resultados = []
        for l in lineas:
            elements = l.split(',')
            variables = {}
            for e in elements:
                variables[e.split('=')[0]] = e.split('=')[1]
            self.resultados.append(variables)

        plt.rcdefaults()

    def resultadosPorMapa(self):
        s = sorted(self.resultados, key=lambda r: r['id'])
        l = {}
        while len(s) != 0:
            r = s.pop(0)
            if r['id'] in l.keys():
                l[r['id']].append(r)
            else :
                l[r['id']] = [r]

        j = 0
        for lol in l.items():
            algoritmos = [r['algoritmo'] for r in lol[1]]
            iteraciones = [int(r['it']) for r in lol[1]]
            distancias = [float(r['distancia']) for r in lol[1]]

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
            ax.set_title('distancia de la ruta hallada para el mapa {0}'.format(lol[0]))
            plt.plot(distancias, y_pos, 'bo')
        plt.show()

    def pintar(self):
        fig, ax = plt.subplots()
        ids = [r['id'] for r in self.resultados]

        y_pos = np.arange(len(ids))
        iteraciones = [int(r['it']) for r in self.resultados]
        error = np.random.rand(len(ids))

        ax.barh(y_pos, iteraciones, xerr=error, align='center',
                color='green', ecolor='black')
        ax.set_yticks(y_pos)
        ax.set_yticklabels(ids)
        ax.invert_yaxis()  # labels read top-to-bottom
        ax.set_xlabel('Performance')
        ax.set_title('How fast do you want to go today?')
        plt.show()
if __name__ == '__main__':
    e = Estadisticas()
    # e.resultadosPorMapa()


