import cost_function
import distance_correlation
import grid_search as gs
import multiprocess_local_search as ls
import numpy as np
import bati
import distance_correlation
from variables import *


m_heur = 10

##### Restriction du domaine par path_finding
distance_field=np.load('distance_field.npy')
corr_mat = distance_correlation.correlation(distance_field,SOURCE_PATH)


x_min = 100       # Le domaine exploré sera compris entre x_min,x_max y_min et y_max.
x_max = 0
y_min = 100
y_max = 0

for x in range(len(corr_mat)):
    for y in range(len(corr_mat[0])):
        if bati.test_point_inside(x,y)==0 and corr_mat[x][y]>threshold:
            x_min = min(x,x_min)
            x_max = max(x,x_max)
            y_min = min(y,y_min)
            y_max = max(y,y_max)
domain = (x_min,x_max,y_min,y_max)
print(f'searching the domain : {domain}')
##### Potentielle grid-search
grid_p, grid_c = gs.grid_search(SOURCE_PATH,domain,m_heur,pas_gs) # renvoie une liste de point/coût


##### Définitions des points de départ de la recherche locale
nb_point = min(len(grid_p),3)
starting_points = []  # On selectionne les points prometteurs
for k in range (nb_point):
    i = np.argmin(np.array(grid_c))
    starting_points.append(grid_p.pop(i))
    grid_c.pop(i)
print(f'continuing with points {starting_points}')
##### Etape finale de recherche locale
cost = []
points = []

ls_results = ls.batch_local_search(SOURCE_PATH, starting_points, m_heur)

#for point in starting_points:
#    print('launching local search for points', point)
#    p,c = ls.local_search(SOURCE_PATH,point,m_heur)
#    points.append(p)
#    cost.append(c)

#res = (points[np.argmin(np.array(cost))],min(cost))
print(ls_results)
print('estimated source position', min(ls_results, key = lambda x:x[1]))
