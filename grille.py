
from voiture import *
problem_set_path = "./Problem/problem_set.txt"

class Board:
    def __init__(self, rows=6, cols=6):
        self.rows = rows
        self.cols = cols
        self.grid = []
        self.makeGrid(self.rows +1)
        self.level = 0
        self.voitures = {}
        self.stages = []

        with open(problem_set_path, "r") as etape:
            for line in etape:
                mots = line.split(" ")
                stage = []
                for chaine in mots:
                    chaine = chaine.strip()
                    block = []
                    for carac in chaine:
                        if carac.isdigit():
                            block.append(int(carac))
                        else:
                            block.append(carac)
                    stage.append(block)
                self.stages.append(stage)

    def __str__(self):
        ret_str = "\n"
        for i in range(self.rows):
            for j in range(self.cols):
                ret_str += str(self.grid[j][i])
                ret_str +=" "
            ret_str += "\n"
        ret_str +="\n"
        return ret_str

    def makeGrid(self, size: int) -> None:
        """
        Crée une grille carrée de taille `size` et l'initialise avec des zéros.

        Arguments :
        - size (int) : la taille de la grille (nombre de lignes et de colonnes).

        Exemple :
        >>> b = Board()
        >>> b.makeGrid(3)
        >>> b.grid
        [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        """
        self.grid = []
        for i in range(size):
            row = [0] * size
            self.grid.append(row)

    def preparation_niveau(self):
        """
        Prépare le niveau actuel en plaçant toutes les voitures sur la grille à partir des données chargées.
        Réinitialise la grille et le dictionnaire des voitures.

        Exemple :
        >>> b = Board()
        >>> b.level = 0
        >>> b.preparation_niveau()
        """
        self.efface_Grid()
        self.voitures = {}
        niveaux_courant = self.stages[self.level]
        for v in niveaux_courant:
            self.pousse_voiture(Voiture(v[0], [v[1], v[2]], v[3]))

    def reset(self):
        """
        Réinitialise le niveau actuel (redémarre le plateau à l’état initial).
        """
        self.preparation_niveau()

    def pousse_voiture(self, voiture):
        """
        Tente d’ajouter une voiture sur la grille selon sa position et sa direction.

        Arguments :
        - voiture (Voiture) : l'objet voiture à placer.

        Retour :
        - bool : True si la voiture a été placée avec succès, False sinon.
        """
        vPos = voiture.posi
        vLen = voiture.len
        vDir = voiture.direction
        vKind = voiture.kind

        if vKind in self.voitures:
            return False

        if vDir == 'h':
            if not (0 <= vPos[0] < self.cols - vLen + 1 and 0 <= vPos[1] < self.rows):
                return False
            for i in range(vPos[0], vPos[0] + vLen):
                if self.grid[i][vPos[1]] != 0:
                    return False
            self.voitures[vKind] = voiture
            for i in range(vPos[0], vPos[0] + vLen):
                self.grid[i][vPos[1]] = vKind

        elif vDir == 'v':
            if not (0 <= vPos[0] < self.cols and 0 <= vPos[1] < self.rows - vLen + 1):
                return False
            for i in range(vPos[1], vPos[1] + vLen):
                if self.grid[vPos[0]][i] != 0:
                    return False
            self.voitures[vKind] = voiture
            for i in range(vPos[1], vPos[1] + vLen):
                self.grid[vPos[0]][i] = vKind

        return True

    def efface_Grid(self):
        """
        Réinitialise la grille en mettant toutes ses cases à 0.

        Exemple :
        >>> b = Board()
        >>> b.grid = [[1, 2], [3, 4]]
        >>> b.efface_Grid()
        >>> b.grid
        [[0, 0], [0, 0]]
        """
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                self.grid[i][j] = 0

    def isOnboard(self, kind: str) -> bool:
        """
        Vérifie si un type de véhicule est présent sur le plateau.

        Arguments :
        - kind (str) : le nom du véhicule à vérifier.

        Retour :
        - bool : True si présent, False sinon.

        Exemple :
        >>> b = Board()
        >>> b.voitures = {'a': Voiture('a', [0,0], 'h')}
        >>> b.isOnboard('a')
        True
        """
        return kind in self.voitures

    def deplace_voiture(self, kind, val):
        """
        Permet de déplacer une voiture d'une certaine valeur si le déplacement est valide.

        Arguments :
        - kind (str) : identifiant du véhicule.
        - val (int) : déplacement (+1, -1, etc.).

        Retour :
        - bool : True si le déplacement a été effectué, False sinon.
        """
        if kind not in self.voitures:
            return False

        voiture = self.voitures[kind]
        vPos = voiture.posi[:]
        vLen = voiture.len
        vDir = voiture.direction

        if vDir == 'h':
            if vPos[0] + val < 0 or vPos[0] + val + vLen > self.cols:
                return False
            for i in range(vPos[0] + val, vPos[0] + val + vLen):
                if self.grid[i][vPos[1]] != 0 and self.grid[i][vPos[1]] != kind:
                    return False
            for i in range(vPos[0], vPos[0] + vLen):
                self.grid[i][vPos[1]] = 0
            voiture.posi[0] += val
            for i in range(voiture.posi[0], voiture.posi[0] + vLen):
                self.grid[i][voiture.posi[1]] = kind
            return True

        elif vDir == 'v':
            if vPos[1] + val < 0 or vPos[1] + val + vLen > self.rows:
                return False
            for i in range(vPos[1] + val, vPos[1] + val + vLen):
                if self.grid[vPos[0]][i] != 0 and self.grid[vPos[0]][i] != kind:
                    return False
            for i in range(vPos[1], vPos[1] + vLen):
                self.grid[vPos[0]][i] = 0
            voiture.posi[1] += val
            for i in range(voiture.posi[1], voiture.posi[1] + vLen):
                self.grid[voiture.posi[0]][i] = kind
            return True

    def isLevelCleared(self):
        """
        Vérifie si la voiture rouge ('x') est complètement sortie du plateau (position au moins en [5,2]).
        Retour :
        - bool : True si le niveau est terminé, False sinon.
        """
        if 'x' not in self.voitures:
            return False

        voiture_x = self.voitures['x']

        # Si la voiture est horizontale
        if voiture_x.direction == 'h':
            x_start = voiture_x.posi[0]
            x_end = x_start + voiture_x.len - 1

            # La sortie est à (6,2), donc on vérifie si la voiture atteint cette position
            return voiture_x.posi[1] == 2 and x_end == 5
        return False

    #     def get_state(self):
    #         """
    #         Retourne un tuple représentant l’état actuel du plateau.
    #         Chaque élément est une description d’un véhicule (type, x, y).
    # 
    #         Retour :
    #         - tuple : état unique du plateau.
    # 
    #         Exemple :
    #         >>> b = Board()
    #         >>> b.preparation_niveau()
    #         >>> b.get_state()
    #         (('a', 0, 0), ('x', 1, 2), ...)
    #         """
    #         etat = []
    #         voitures_tries = sorted(self.voitures.values(), key=lambda v: v.kind)
    #         for v in voitures_tries:
    #             etat.append((v.kind, v.posi[0], v.posi[1]))
    #         return tuple(etat)
    def get_state(self):
        """
        Représente l’état du plateau sous une forme compacte et unique,
        en listant les positions des voitures triées par leur identifiant.

        Cela permet de comparer facilement deux états du jeu, par exemple
        pour vérifier si une configuration a déjà été explorée.

        Retour :
        - tuple : état compressé, chaque élément est un tuple (identifiant, x, y)

        Exemple :
        >>> b = Board()
        >>> b.level = 0
        >>> b.preparation_niveau()
        >>> b.get_state()
        (('a', 0, 0), ('b', 2, 3), ('x', 1, 2))
        """
        return tuple((k, v.posi[0], v.posi[1]) for k, v in sorted(self.voitures.items()))

    def afficher_terminal(self):
        for y in range(self.rows):
            ligne = ""
            for x in range(self.cols):
                cell = self.grid[x][y]
                ligne += str(cell) if cell != 0 else "."
                ligne += " "
            print(ligne)
    def clone(self):
        """
        Crée une copie rapide et peu coûteuse du plateau (Board), sans utiliser deepcopy.
        Retour :
        - Board : une nouvelle instance avec les mêmes voitures et grille.
        """
        new_board = Board(self.rows, self.cols)
        new_board.level = self.level
        new_board.stages = self.stages  # Les stages ne changent jamais, donc pas besoin de copier
        new_board.grid = [row[:] for row in self.grid]  # Copie rapide ligne par ligne
        new_board.voitures = {
            k: Voiture(v.kind, v.posi[:], v.direction) for k, v in self.voitures.items()
        }
        return new_board

