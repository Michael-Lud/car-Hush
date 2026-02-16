MAX_COLS = 6
MAX_ROWS = 6

import pygame
from pygame.locals import *

class Voiture:
    """
    Classe représentant une voiture sur la grille du jeu Rush Hour.

    Attributs :
        kind (str) : Identifiant de la voiture (ex: 'x', 'a', ..., 'r').
        posi (list[int, int]) : Position [x, y] de la voiture sur la grille.
        direction (str) : Orientation de la voiture, 'h' pour horizontal ou 'v' pour vertical.
        len (int) : Longueur de la voiture (2 ou 3).
        image (pygame.Surface) : Image chargée et orientée de la voiture.
    """

    def __init__(self, kind, posi, direction):
        """
        Initialise une voiture avec son type, sa position et sa direction.

        Args:
            kind (str) : Le type de voiture (doit correspondre à un nom d'image dans ./img/).
            posi (list[int, int]) : La position initiale [x, y] sur la grille (0-indexé).
            direction (str) : 'h' pour horizontal, 'v' pour vertical.

        Raises:
            Exception: Si le type, la position ou la direction ne sont pas valides.
        """
        if type(kind) is str:
            self.kind = kind
            if self.kind in "xabcdefghijkopqr":
                self.len = 2 if self.kind in "xabcdefghijk" else 3
                self.img_name = f"./img/{self.kind}.png"
            else:
                raise Exception(f"{kind} does not belong to any known kind")
        else:
            raise Exception(f"{kind} is not a string")

        if direction in ("h", "v"):
            self.direction = direction
        else:
            raise Exception("Direction should be either 'h' (horizontal) or 'v' (vertical)")

        if isinstance(posi, list) and len(posi) == 2:
            if 0 <= posi[0] < MAX_COLS and 0 <= posi[1] < MAX_ROWS:
                self.posi = [posi[0], posi[1]]
            else:
                raise Exception(f"{posi} is not in a valid grid range")
        else:
            raise Exception("Position should be a list of two integers [x, y]")

        # Chargement et ajustement de l'image avec Pygame
        self.image = pygame.image.load(self.img_name)
        self.image = pygame.transform.scale(self.image, (self.len * 100, 100))
        if self.direction == 'v':
            self.image = pygame.transform.rotate(self.image, 90)
    
    def copy(self):
        return Voiture(self.kind, self.posi[:], self.direction)
    
    def __repr__(self):
        """
        Retourne une représentation textuelle de la voiture.

        Returns:
            str: Une chaîne décrivant l'objet Voiture.

        Exemple :
        >>> v = Voiture("x", [2, 0], "h")
        >>> print(v)
        Voiture(kind='x', posi=[2, 0], direction='h')
        """
        return f"Voiture(kind='{self.kind}', posi={self.posi}, direction='{self.direction}')"
    