import math

# Fonctions utiles
def arrondi():
    return int(input("À quelle décimale veux-tu arrondir ? "))

def saisir_point(nom_point):
    x = float(input(f"Coordonnée x de {nom_point} : "))
    y = float(input(f"Coordonnée y de {nom_point} : "))
    return x, y

# Choix de l'utilisateur
choix = input("""1 somme de vecteurs
2 coordonnées d'un vecteur
3 norme d'un vecteur
4 produit scalaire géométrique
5 produits scalaire dans un repère orthonormé
6 définir si deux vecteurs sont ou non colinéaires
7 calculer le déterminant de deux vecteurs
8 établir le théorème d'al-kashi pour trouver un côté
9 établir le théorème d'al-kashi pour trouver un angle
10 calculer la projection orthogonale OH
Quel est ton choix ? """)

if choix == "1":
    xa, ya = saisir_point("A")
    xb, yb = saisir_point("B")
    x = xa + xb
    y = ya + yb
    arrondir_à = arrondi()
    print(f"""u + v = (x1 + x2 ; y1 + y2)
u + v = ({round(x, arrondir_à)} ; {round(y, arrondir_à)})""")

elif choix == "2":
    x1 = int(input("Coordonnée xa : "))
    x2 = int(input("Coordonnée xb : "))
    y1 = int(input("Coordonnée ya : "))
    y2 = int(input("Coordonnée yb : "))
    x = x2 - x1
    y = y2 - y1
    print(f"AB = ({x} ; {y})")

elif choix == "3":
    choix2 = input("Utilises-tu les coordonnées de deux points (1) ou d'un vecteur (2) ? ")
    if choix2 == "1":
        x1 = int(input("Coordonnée xa : "))
        x2 = int(input("Coordonnée xb : "))
        y1 = int(input("Coordonnée ya : "))
        y2 = int(input("Coordonnée yb : "))
        x = x2 - x1
        y = y2 - y1
        u = math.sqrt(x**2 + y**2)
        print(f"AB = ({x} ; {y})")
        print(f"||AB|| = √({x}² + {y}²) = √{x**2 + y**2} = {u}")
    elif choix2 == "2":
        x = int(input("x = ? "))
        y = int(input("y = ? "))
        r = math.sqrt(x**2 + y**2)
        print(f"u = √({x**2} + {y**2}) = √{x**2 + y**2} = {r}")
