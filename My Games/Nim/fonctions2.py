lst = [7, 5, 3, 1]


def initialisation_du_jeu(col, lst):
    l = []
    for i in range(col):
        l.append([])
        for j in range(lst[i]):
            l[i].append(j+1)
    return l

def joueur(n):
    n = n % 2
    return n

def coup_possible(n, lst, col=0):
    if int(n) > len(lst[col]):
        return False
    return True

def coup_par_col(lst):
    lst_col = []
    for i in range(len(lst)):
        lst_col.append(i+1)
    return lst_col

def verif_col(lst, lst_col):
    for e in lst_col:
        if lst[e-1] == []:
            lst_col.remove(e)
    return lst_col

def retire_batons(nb, lst):
    del lst[-nb:]
    return lst

def fin_de_manche(lst):
    for i in range(len(lst)):
        if len(lst[i]) != 0:
            return True
    return False

def joueur_gagnant(n, mode):
    if mode == 1:
        if n == 0:
            n=2
        return n
    if n == 1:
        return 2
    return 1

def point_joueur(point, j1, j2):
    if point == 1:
        return j1+1, j2
    return j1, j2+1
