from v2menugraph import*


largeur = 800
hauteur = 600


fltk.cree_fenetre(largeur, hauteur)


n = 0
col = 0
lin = []
lst = []
lst_coup = [0]
while True:
    n, lst = menu(n, lst, largeur, hauteur, lin)
    if len(lst) == 2 and n == 2:
        largeur, hauteur = lst[0], lst[1]
        fltk.ferme_fenetre()
        fltk.cree_fenetre(largeur, hauteur)
    elif col != 0 and len(lst) == col:
        lin = lst
    elif len(lst) == 4:
        adversaire, m, variante, mode = lst[0], lst[1], lst[2], lst[3]
        if variante == 0:
            col, lin = 1, [21]
        elif variante == 1:
            col, lin = 4, [7, 5, 3, 1]
    elif variante == 2 and len(lst) == 1:
        col = int(lst[0])
    if n == 7:
        lst_coup = lst
        break
    
print(lst_coup)
liste_de_jeu = initialisation_du_jeu(col, lin)


if lst_coup[0] == 0:
    for e in liste_de_jeu:
        if lst_coup[-1] < e[-1]:
            lst_coup = []
            for i in range(e[-1]):
                lst_coup.append(i+1)
print(lst_coup)
partie(largeur, hauteur, liste_de_jeu, adversaire, m, variante, mode, lst_coup)

fltk.ferme_fenetre()








