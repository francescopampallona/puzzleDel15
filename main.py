'''
PUZZLE DEL 15
LE MOSSE RIGUARDANO LO SPOSTAMENTO DELLO 0 LUNGO IL PUZZLE
MOSSE POSSIBILI (applicate quando possibile):
0)SPOSTAMENTO IN ALTO
1)SPOSTAMENTO A DESTRA
2)SPOSTAMENTO A SINISTRA
3)SPOSTAMENTO IN BASSO
'''
import copy
from heapq import heappush, heappop


def compiAzione(scelta, stato):
    stato_risultante=copy.deepcopy(stato)
    # Trova la posizione dello zero
    riga, colonna=trovaPosizioneNumero(stato_risultante,0)
    if(str(scelta).lower()=="w"):
        if(riga>0):
          valore_da_scambiare=stato_risultante[riga-1][colonna]
          stato_risultante[riga - 1][colonna]=0
          stato_risultante[riga][colonna]=valore_da_scambiare
    elif(str(scelta).lower()=="d"):
        if(colonna<3):
          valore_da_scambiare = stato_risultante[riga][colonna+1]
          stato_risultante[riga][colonna+1] = 0
          stato_risultante[riga][colonna] = valore_da_scambiare
    elif(str(scelta).lower()=="a"):
        if(colonna>0):
          valore_da_scambiare = stato_risultante[riga][colonna - 1]
          stato_risultante[riga][colonna - 1] = 0
          stato_risultante[riga][colonna] = valore_da_scambiare
    elif(str(scelta).lower()=="s"):
        if(riga<3):
          valore_da_scambiare = stato_risultante[riga + 1][colonna]
          stato_risultante[riga + 1][colonna] = 0
          stato_risultante[riga][colonna] = valore_da_scambiare
    else:
        pass
    return stato_risultante

def trovaPosizioneNumero(stato, numero):
    for i, row in enumerate(stato):
        for j, value in enumerate(row):
            if value == numero:
                return (i, j)
    return None

def obiettivoRaggiunto(stato):
    stato_obiettivo=[[1,2,3,4],
                     [5,6,7,8],
                     [9,10,11,12],
                     [13,14,15,0]]
    if(stato==stato_obiettivo):
        return True
    else:
        return False


def calcoloDistanzaManhattan(stato):
    # Mappatura delle posizioni desiderate nello stato obiettivo
    stato_obiettivo = {
        1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (0, 3),
        5: (1, 0), 6: (1, 1), 7: (1, 2), 8: (1, 3),
        9: (2, 0), 10: (2, 1), 11: (2, 2), 12: (2, 3),
        13: (3, 0), 14: (3, 1), 15: (3, 2), 0: (3, 3)
    }
    distanzaManhattanTotale = 0
    # Scansiona lo stato corrente per trovare la posizione di ogni tassello
    for i, row in enumerate(stato):
        for j, valore in enumerate(row):
            if valore != 0:  # Ignora il tassello vuoto
                riga_desiderata, colonna_desiderata = stato_obiettivo[valore]
                distanzaManhattanTotale += abs(i - riga_desiderata) + abs(j - colonna_desiderata)

    return distanzaManhattanTotale
def mostraStato(stato):
    for riga in stato:
        print(" ".join(f"{valore:2}" for valore in riga))

def game(stato_iniziale):
  stato = stato_iniziale
  print("Scegli mosse con wdas")
  while(not obiettivoRaggiunto(stato)):
      mossa = input()
      stato = compiAzione(mossa, stato)
      mostraStato(stato)
      print(f"Distanza manhattan: {calcoloDistanzaManhattan(stato)}")
  print("PUZZLE RISOLTO.COMPLIMENTI :)")


def aStarSearch(stato_iniziale):

    def costo(stato):
        return calcoloDistanzaManhattan(stato)

    coda = []
    heappush(coda, (costo(stato_iniziale), 0, stato_iniziale, []))  # (f(n), g(n), stato, percorso)
    statiVisitati = set()
    statiVisitati.add(tuple(map(tuple, stato_iniziale)))

    while coda:
        _, g, stato, percorso = heappop(coda)

        if obiettivoRaggiunto(stato):
            print(f"OBIETTIVO RAGGIUNTO IN {len(percorso)} MOSSE!")
            for passo, mossa in enumerate(percorso):
                print(f"Mossa {passo + 1}: {mossa}")
            mostraStato(stato)
            return

        for mossa in ["w","a","s","d"]:
            stato_nuovo = compiAzione(str(mossa), stato)
            stato_tupla = tuple(map(tuple, stato_nuovo))
            if stato_tupla not in statiVisitati:
                statiVisitati.add(stato_tupla)
                heappush(coda, (g + 1 + costo(stato_nuovo), g + 1, stato_nuovo, percorso + [mossa]))

    print("Impossibile trovare la soluzione.")

STATO_INIZIALE = [[8,14,7,5],
                  [6,3,4,9],
                  [1,12,0,10],
                  [2,13,15,11]]
mostraStato(STATO_INIZIALE)
print(f"Distanza manhattan: {calcoloDistanzaManhattan(STATO_INIZIALE)}")
print("Scegli:")
print("1)Prova a risolvere tu")
print("2)Risolvi con algoritmo di ricerca A star")
scelta=input()
if(scelta=="1"):
    game(STATO_INIZIALE)
elif(scelta=="2"):
    aStarSearch(STATO_INIZIALE)