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
  y1 = int(input("coordonnée y1"))
  x2 = int(input("coordonnée x2"))
  y2 = int(input("coordonnée y2"))
  x = x1 + x2
  y = y1 + y2
  print("""u+v = (x1+x2;y1+y2)
  u+v = ({x} ; {y})""") 
