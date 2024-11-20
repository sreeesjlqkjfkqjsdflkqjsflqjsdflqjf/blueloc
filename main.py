from bluepy.btle import Scanner, DefaultDelegate
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.patches as mpatches
from tabulate import tabulate
import time
import numpy as np
nb_scan = 10
pair_valeur_addr = []
valeurs = []
scanner = Scanner()
def decouverte():
    scan = scanner.scan(timeout=1)
    arr = [[s.addr, s.rssi] for s in scan]
    print(tabulate(arr, headers = ["addresse", "rssi"], tablefmt="heavy_grid"))

def fait_un_point():
    for n in range(nb_scan):
        scan = scanner.scan(timeout=1)
        for s in scan:
            if str(s.addr)[:5]=="88:6b" and str(s.addr) not in pair_valeur_addr:
                pair_valeur_addr.append(str(s.addr))
                valeurs.append([s.rssi])
            elif str(s.addr)[:5]=="88:6b":
                valeurs[pair_valeur_addr.index(str(s.addr))].append(s.rssi)


    for v in valeurs:
        plt.plot(range(nb_scan), v)
    plt.show()
    print(tabulate([[pair_valeur_addr[i], np.mean(valeurs[i]), np.std(valeurs[i])] for i in range(len(valeurs))], headers = ["addresse", "moyenne", "déviation"], tablefmt="heavy_grid"))
def affiche(cercles):
    fig, ax = plt.subplots()
    ax.imshow(mpimg.imread("./Screenshot_2024-11-12_12-04-42.png"))
    c = mpatches.Circle((0, 0), 200, color='r')
    ax.add_patch(c)
    plt.show()

if __name__ == "__main__":
    début = time.time()
    # scan()
    # decouverte()
    fait_un_point()
    print(f"{time.time()-début} secondes")
    affiche([])
