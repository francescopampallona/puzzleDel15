import java.util.*;

public class Main {

    public static void main(String[] args) {
        int[][] statoIniziale = {
                {8, 14, 7, 5},
                {6, 3, 4, 9},
                {1, 12, 0, 10},
                {2, 13, 15, 11}
        };

        mostraStato(statoIniziale);
        System.out.println("Distanza Manhattan: " + calcoloDistanzaManhattan(statoIniziale));
        System.out.println("Scegli:");
        System.out.println("1) Prova a risolvere tu");
        System.out.println("2) Risolvi con algoritmo di ricerca A*");

        Scanner scanner = new Scanner(System.in);
        String scelta = scanner.nextLine();

        if (scelta.equals("1")) {
            game(statoIniziale);
        } else if (scelta.equals("2")) {
            aStarSearch(statoIniziale);
        }
    }

    public static int[][] compiAzione(String scelta, int[][] stato) {
        int[][] statoRisultante = copiaStato(stato);
        int[] posizioneZero = trovaPosizioneNumero(statoRisultante, 0);
        int riga = posizioneZero[0], colonna = posizioneZero[1];

        switch (scelta.toLowerCase()) {
            case "w":
                if (riga > 0) {
                    scambia(statoRisultante, riga, colonna, riga - 1, colonna);
                }
                break;
            case "d":
                if (colonna < 3) {
                    scambia(statoRisultante, riga, colonna, riga, colonna + 1);
                }
                break;
            case "a":
                if (colonna > 0) {
                    scambia(statoRisultante, riga, colonna, riga, colonna - 1);
                }
                break;
            case "s":
                if (riga < 3) {
                    scambia(statoRisultante, riga, colonna, riga + 1, colonna);
                }
                break;
        }
        return statoRisultante;
    }

    public static int[] trovaPosizioneNumero(int[][] stato, int numero) {
        for (int i = 0; i < stato.length; i++) {
            for (int j = 0; j < stato[i].length; j++) {
                if (stato[i][j] == numero) {
                    return new int[]{i, j};
                }
            }
        }
        return null;
    }

    public static boolean obiettivoRaggiunto(int[][] stato) {
        int[][] statoObiettivo = {
                {1, 2, 3, 4},
                {5, 6, 7, 8},
                {9, 10, 11, 12},
                {13, 14, 15, 0}
        };
        return Arrays.deepEquals(stato, statoObiettivo);
    }

    public static int calcoloDistanzaManhattan(int[][] stato) {
        int[][] statoObiettivo = {
                {1, 2, 3, 4},
                {5, 6, 7, 8},
                {9, 10, 11, 12},
                {13, 14, 15, 0}
        };
        Map<Integer, int[]> mappaObiettivo = new HashMap<>();
        for (int i = 0; i < statoObiettivo.length; i++) {
            for (int j = 0; j < statoObiettivo[i].length; j++) {
                mappaObiettivo.put(statoObiettivo[i][j], new int[]{i, j});
            }
        }

        int distanzaTotale = 0;
        for (int i = 0; i < stato.length; i++) {
            for (int j = 0; j < stato[i].length; j++) {
                int valore = stato[i][j];
                if (valore != 0) {
                    int[] posizioneDesiderata = mappaObiettivo.get(valore);
                    distanzaTotale += Math.abs(i - posizioneDesiderata[0]) + Math.abs(j - posizioneDesiderata[1]);
                }
            }
        }
        return distanzaTotale;
    }

    public static void mostraStato(int[][] stato) {
        for (int[] riga : stato) {
            for (int valore : riga) {
                System.out.print(String.format("%2d ", valore));
            }
            System.out.println();
        }
    }

    public static void game(int[][] statoIniziale) {
        Scanner scanner = new Scanner(System.in);
        int[][] stato = copiaStato(statoIniziale);

        System.out.println("Scegli mosse con wdas");
        while (!obiettivoRaggiunto(stato)) {
            String mossa = scanner.nextLine();
            stato = compiAzione(mossa, stato);
            mostraStato(stato);
            System.out.println("Distanza Manhattan: " + calcoloDistanzaManhattan(stato));
        }
        System.out.println("PUZZLE RISOLTO. COMPLIMENTI :)");
    }

    public static void aStarSearch(int[][] statoIniziale) {
        PriorityQueue<Nodo> coda = new PriorityQueue<>();
        Set<String> statiVisitati = new HashSet<>();

        coda.add(new Nodo(statoIniziale, 0, calcoloDistanzaManhattan(statoIniziale), new ArrayList<>(), new ArrayList<>()));
        statiVisitati.add(statoToString(statoIniziale));

        while (!coda.isEmpty()) {
            Nodo nodo = coda.poll();

            if (obiettivoRaggiunto(nodo.stato)) {
                System.out.println("OBIETTIVO RAGGIUNTO IN " + nodo.percorso.size() + " MOSSE!");
                for (int i = 0; i < nodo.percorso.size(); i++) {
                    System.out.println("Mossa " + (i + 1) + ": " + nodo.percorso.get(i));
                    mostraStato(nodo.statiAttraversati.get(i));
                }
                return;
            }

            for (String mossa : Arrays.asList("w", "a", "s", "d")) {
                int[][] statoNuovo = compiAzione(mossa, nodo.stato);
                String statoStringa = statoToString(statoNuovo);

                if (!statiVisitati.contains(statoStringa)) {
                    statiVisitati.add(statoStringa);
                    List<String> nuovoPercorso = new ArrayList<>(nodo.percorso);
                    List<int[][]> nuovoPercorsoStati = new ArrayList<>(nodo.statiAttraversati);
                    nuovoPercorso.add(mossa);
                    nuovoPercorsoStati.add(statoNuovo);
                    coda.add(new Nodo(statoNuovo, nodo.costo + 1, nodo.costo + 1 + calcoloDistanzaManhattan(statoNuovo), nuovoPercorso, nuovoPercorsoStati));
                }
            }
        }
        System.out.println("Impossibile trovare la soluzione.");
    }

    public static String statoToString(int[][] stato) {
        StringBuilder sb = new StringBuilder();
        for (int[] riga : stato) {
            for (int valore : riga) {
                sb.append(valore).append(",");
            }
        }
        return sb.toString();
    }

    public static int[][] copiaStato(int[][] stato) {
        int[][] copia = new int[stato.length][stato[0].length];
        for (int i = 0; i < stato.length; i++) {
            System.arraycopy(stato[i], 0, copia[i], 0, stato[i].length);
        }
        return copia;
    }

    public static void scambia(int[][] stato, int riga1, int colonna1, int riga2, int colonna2) {
        int temp = stato[riga1][colonna1];
        stato[riga1][colonna1] = stato[riga2][colonna2];
        stato[riga2][colonna2] = temp;
    }

    static class Nodo implements Comparable<Nodo> {
        int[][] stato;
        int costo;
        int stimaTotale;
        List<String> percorso;

        List<int[][]> statiAttraversati;

        public Nodo(int[][] stato, int costo, int stimaTotale, List<String> percorso, List<int[][]> statiAttraversati) {
            this.stato = copiaStato(stato);
            this.costo = costo;
            this.stimaTotale = stimaTotale;
            this.percorso = percorso;
            this.statiAttraversati= statiAttraversati;
        }

        @Override
        public int compareTo(Nodo o) {
            return Integer.compare(this.stimaTotale, o.stimaTotale);
        }
    }
}
