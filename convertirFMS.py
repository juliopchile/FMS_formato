import numpy as np
import json


path = "FMS\ESP T4_J4 SweetPain vs Gazir 2020"
#path = "FMS\MC 1 vs MC 2"

def shuffle_slices(data, round, slices):
    idx = 0
    for slice_indices in slices:
        start, end = slice_indices
        if start != end:
            length = end - start
            round[idx:idx+length] = data[start:end]
            idx += length
        else:  # If the slice length is 1
            round[idx] = data[start]
            idx += 1


def leer_FMS(path):
    '''
    Lee archivos creados por FMS Votación 3.4 y los devuelve ordenados más legible
    '''
    with open(path, 'r') as file:
        data = file.read().split('|')
        data.reverse()

    mc1 = data.pop()
    mc2 = data.pop()

    if data[28] == mc1:     # Empieza MC_1 la réplica
        replica_flag = 1
    elif data[28] == mc2:   # Empieza MC_2 la réplica
        replica_flag = 2
    else:                   # No hay réplica
        replica_flag = 0

    # Arreglos
    easymode =  np.zeros(18, dtype=float)
    hardmode =  np.zeros(18, dtype=float)
    tematica1 = np.zeros(14, dtype=float)
    tematica2 = np.zeros(14, dtype=float)
    random =    np.zeros(22, dtype=float)
    minutos1 =  np.zeros(24, dtype=float)
    minutos2 =  np.zeros(24, dtype=float)
    deluxe =    np.zeros(28, dtype=float)
    replica =   np.zeros(18, dtype=float)

    # Indices
    slices_easymode = [(162, 168), (174, 177), (168, 174), (177, 180)]
    slices_hardmode = [(180, 186), (192, 195), (186, 192), (195, 198)]
    slices_tematica1 = [(202, 206), (214, 217), (208, 212), (217, 220)]
    slices_tematica2 = [(220, 224), (232, 235), (226, 230), (235, 238)]
    slices_random = [(138, 142), (212, 214), (3, 3), (1, 1), (146, 149), (142, 146), (230, 232), (2, 2), (0, 0), (149, 152)]
    slices_minuto1 = [(110, 116), (122, 125), (116, 122), (125, 128), (57, 57), (56, 56), (55, 55), (52, 55)]
    slices_minuto2 = [(128, 134), (154, 157), (134, 138), (152, 154), (157, 160), (46, 52)]
    slices_deluxe = [(90, 94), (106, 108), (80, 83), (86, 88), (98, 101), (94, 98), (108, 110), (83, 86), (88, 90), (101, 104)]
    slices_replica = [(60, 64), (76, 78), (68, 71), (64, 68), (78, 80), (71,74)]

    # Ordenamiento
    shuffle_slices(data, easymode, slices_easymode)
    shuffle_slices(data, hardmode, slices_hardmode)
    shuffle_slices(data, tematica1, slices_tematica1)
    shuffle_slices(data, tematica2, slices_tematica2)
    shuffle_slices(data, random, slices_random)
    shuffle_slices(data, minutos1, slices_minuto1)
    shuffle_slices(data, minutos2, slices_minuto2)
    shuffle_slices(data, deluxe, slices_deluxe)
    shuffle_slices(data, replica, slices_replica)

    # Se junta todo
    batalla = {"MC1": mc1, "MC2": mc2, "flag": replica_flag, "EasyMode": easymode.tolist(), "HardMode": hardmode.tolist(), "Tematica 1": tematica1.tolist(),
               "Tematica 2": tematica2.tolist(), "RandomMode": random.tolist(), "Minutos 1": minutos1.tolist(), "Minutos 2": minutos2.tolist(),
               "Deluxe": deluxe.tolist(), "Replica": replica.tolist()}
    return batalla


if __name__ == "__main__":
    batalla = leer_FMS(path)

    mc1 = batalla["MC1"]
    mc2 = batalla["MC2"]
    flag = batalla["flag"]
    
    print(f"{batalla}")
    
    with open(path+".json", "w") as file:
        json.dump(batalla, file)
