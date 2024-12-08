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


def compiAzione(scelta, stato):
    stato_risultante=copy.copy(stato)
    # Trova la posizione dello zero
    riga, colonna=(0,0)
    for i, row in enumerate(stato_risultante):
        for j, value in enumerate(row):
            if value == 0:
                riga, colonna = (i, j)
                break
    if(scelta=="0" or str(scelta).lower()=="w"):
        if(riga>0):
          valore_da_scambiare=stato_risultante[riga-1][colonna]
          stato_risultante[riga - 1][colonna]=0
          stato_risultante[riga][colonna]=valore_da_scambiare
    elif(scelta=="1" or str(scelta).lower()=="d"):
        if(colonna<3):
          valore_da_scambiare = stato_risultante[riga][colonna+1]
          stato_risultante[riga][colonna+1] = 0
          stato_risultante[riga][colonna] = valore_da_scambiare
    elif(scelta=="2" or str(scelta).lower()=="a"):
        if(colonna>0):
          valore_da_scambiare = stato_risultante[riga][colonna - 1]
          stato_risultante[riga][colonna - 1] = 0
          stato_risultante[riga][colonna] = valore_da_scambiare
    elif(scelta=="3" or str(scelta).lower()=="s"):
        if(riga<3):
          valore_da_scambiare = stato_risultante[riga + 1][colonna]
          stato_risultante[riga + 1][colonna] = 0
          stato_risultante[riga][colonna] = valore_da_scambiare
    else:
        pass
    return stato_risultante

def obiettivoRaggiunto(stato):
    stato_obiettivo=[[1,2,3,4],
                     [5,6,7,8],
                     [9,10,11,12],
                     [13,14,15,0]]
    if(stato==stato_obiettivo):
        return True
    else:
        return False

def mostraStato(stato):
    for riga in stato:
        print(" ".join(f"{valore:2}" for valore in riga))

def game():
  stato_iniziale=[[8,14,7,5],
                  [6,3,4,9],
                  [1,12,0,10],
                  [2,13,15,11]]
  stato = stato_iniziale
  mostraStato(stato)
  print("Scegli mosse con wdas o con 0123")
  while(not obiettivoRaggiunto(stato)):
      mossa = input()
      stato = compiAzione(mossa, stato)
      mostraStato(stato)

game()