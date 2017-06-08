import numpy as np
import matplotlib.pyplot as plt


with open('resultados.dat', 'r') as f:
    lineas = f.readlines()

resultados = []
for l in lineas:
    elements = l.split(',')
    variables = {}
    for e in elements:
        variables[e.split('=')[0]] = e.split('=')[1]
    resultados.append(variables)

plt.rcdefaults()
fig, ax = plt.subplots()

ids = [r['id'] for r in resultados]

y_pos = np.arange(len(ids))
iteraciones = [int(r['it']) for r in resultados]
error = np.random.rand(len(ids))

ax.barh(y_pos, iteraciones, xerr=error, align='center',
        color='green', ecolor='black')
ax.set_yticks(y_pos)
ax.set_yticklabels(ids)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Performance')
ax.set_title('How fast do you want to go today?')

plt.show()
