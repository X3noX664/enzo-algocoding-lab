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
    xua, yua = saisir_point("UA")
    xub, yub = saisir_point("UB")
    xva, yva = saisir_point("VA")
    xvb, yvb = saisir_point("VB")
    xu = xub - xua
    yu = yub - yua
    xv = xvb - xva
    yv = yvb - yva
    arrondir_à = arrondi()
    print(f"""u + v = (xu + xv ; yu + yv)
u + v = ({round(xu + xv, arrondir_à)} ; {round(yu + yv, arrondir_à)})""")

elif choix == "2":
    xa, ya = saisir_point("A")
    xb, yb = saisir_point("B")
    x = xb - xa
    y = yb - ya
    arrondir_à = arrondi()
    print(f"AB = ({round(x, arrondir_à)} ; {round(y, arrondir_à)})")

elif choix == "3":
    choix2 = input("Utilises-tu les coordonnées de deux points (1) ou d'un vecteur (2) ? ")
    if choix2 == "1":
        xa, ya = saisir_point("A")
        xb, yb = saisir_point("B")
        x = xb - xa
        y = yb - ya
        u = math.sqrt(x**2 + y**2)
        arrondir_à = arrondi()
        print(f"AB = ({round(x, arrondir_à)} ; {round(y, arrondir_à)})")
        print(f"||AB|| = √({round(x, arrondir_à)}² + {round(y, arrondir_à)}²) = √{round(x**2 + y**2, arrondir_à)} = {round(u, arrondir_à)}")
        
    elif choix2 == "2":
        x = int(input("x = ? "))
        y = int(input("y = ? "))
        r = math.sqrt(x**2 + y**2)
        arrondir_à = arrondi()
        print(f"u = √({round(x**2, arrondir_à)} + {round(y**2, arrondir_à)}) = √{round(x**2 + y**2, arrondir_à)} = {round(r, arrondir_à)}")
elif choix == "4":
    choix2 = input("utilise tu les coordonnées de vecteurs où l'angle (1) ou les normes (2)")
    if choix2 == "1":
        xa, ya = saisir_point("A")
        xb, yb = saisir_point("B")
        xc, yc = saisir_point("C")
        xd, yd = saisir_point("D")
        angle_deg = float(input("quelle est l'angle entre u et v : ")) 
        angle_rad = math.radians(angle_deg)
        norme_AB = math.sqrt((xb-xa)**2 + (yb-ya)**2)
        norme_CD = math.sqrt((xd-xc)**2 + (yd-yc)**2)
        produit_scalaire = norme_AB * norme_CD * math.cos(angle_rad)
        arrondir_à = arrondi()
        print(round(produit_scalaire, arrondir_à))
    elif choix2 == "2":
        print("test")
