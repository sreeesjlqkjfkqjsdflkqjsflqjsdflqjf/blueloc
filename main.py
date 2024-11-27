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
class Lardon:
    def __init__(self, x, y, addr):
        
        self.mesures = []
        self.dist = 0
        self.x = x 
        self.y = y
        self.addr = addr
    def distance(self):
        avg = sum(self.mesures)/len(self.mesures)
        d = pow(10, abs(avg+58)/(10*2))
        return d
lardons = [Lardon(220, 183, "88:6b:0f:a2:ac:e8"), Lardon(270, 243, "88:6b:0f:a2:b0:31")] 
def decouverte():
    scan = scanner.scan(timeout=1)
    arr = []
    for s in scan:
        if str(s.addr)[:5]=="88:6b":
            arr.append([s.addr, s.rssi])

    print(tabulate(arr, headers = ["addresse", "rssi"], tablefmt="heavy_grid"))

def fait_un_point():
    for n in range(nb_scan):
        scan = scanner.scan(timeout=1)
        for s in scan:
            for lardon in lardons:
                if str(s.addr)==lardon.addr:
                    print(s.addr, lardon.addr, s.rssi)
                    lardon.mesures.append(s.rssi)
    for l in lardons:
        print(l.mesures)
    print(tabulate([[l.addr, l.distance(), np.mean(l.mesures), np.std(l.mesures)] for l in lardons], headers = ["addresse", "distance", "moyenne", "déviation"], tablefmt="heavy_grid"))
def affiche():
    echelle = 20
    fig, ax = plt.subplots()
    ax.imshow(mpimg.imread("./Screenshot_2024-11-12_12-04-42.png"))
    for l in lardons:
        c = mpatches.Circle((l.x, l.y), echelle * l.distance(), color='r', fill=False)
        ax.add_patch(c)
    plt.show()

if __name__ == "__main__":
    début = time.time()
    # scan()
    decouverte()
    fait_un_point()
    print(f"{time.time()-début} secondes")
    affiche()
