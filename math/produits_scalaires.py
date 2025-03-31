 import math
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
quelle est ton choix""")

if choix == "1":
  x1 = int(input("coordonnée x1"))
  x2 = int(input("coordonnée x2"))
  y1 = int(input("coordonnée y1"))
  y2 = int(input("coordonnée y2"))
  x = x1 + x2
  y = y1 + y2
  print(f"""u+v = (x1+x2;y1+y2)
  u+v = ({x} ; {y})""")
elif choix == "2":
  x1 = int(input("coordonnée xa"))
  x2 = int(input("coordonnée xb"))
  y1 = int(input("coordonnée ya"))
  y2 = int(input("coordonnée yb"))
  x = x2 - x1
  y = y2 - y1
  print(f"""AB(xb-xa;yb-ya) 
AB = ({x};{y})""")
elif choix == "3":
  choix2 = input("utilise tu les coordonnées de chaque points (1) ou de chaques vecteurs (2) ?")
  if choix2 == "1":
     x1 = int(input("coordonnée xa"))
     x2 = int(input("coordonnée xb"))
     y1 = int(input("coordonnée ya"))
     y2 = int(input("coordonnée yb"))
     x = x2 - x1
     y = y2 - y1
     print(f"""AB(xb-xa;yb-ya) 
     AB = ({x};{y})""")
     v = x**2 + y**2
     u = math.sqrt(v)
     print(f"""u = √(xb-xa)²+(yb-ya)²)
     = √({x2}-{x1})²+({y2}-{y1})²)
     = {u}""")
                  
