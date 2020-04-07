X_MAX = 100
Y_MAX = 100
RESOLUTION = 1
N_STATION = 5

LINE_COUNT = X_MAX * RESOLUTION
ROW_COUNT = Y_MAX * RESOLUTION
SOURCE_PATH = './TE'

# ---- heuristique ----

threshold = 0.99
TNT_MIN = 1
TNT_MAX = 50

# ---- local search ----
pas_search = 0.2                      #pas de la recherche
pas_tnt = 0.2
pas_sim = 0.2                         #pas de la simu armen
pas_sim_tnt = 0.1                     #pas de la simu armen étape tnt
max_iter_space = 50                   #nb max d'iterations
max_iter_tnt = 50

# ---- grid_search ----
pas_sim_gs = 0.2
pas_gs = 2
