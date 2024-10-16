import fltk
from fonctions2 import*
from bot import*

adversaire = ['Joueur', 'Ordinateur Simple', 'Ordinateur Expert']
quicommence = ['Joueur 1', 'Joueur 2 / Ordinateur']
variante = ['Nim', 'Marienbad', 'Personnalise']
mode = ['Normal', 'Misere']
persocol = ['1', '2', '3', '4', '5', '6', '7', '8', '9']


def menu_de_depart(largeur, hauteur):
    lst = []
    fltk.rectangle(largeur//2-200, hauteur//2-90, largeur//2+200, hauteur//2-40)
    fltk.rectangle(largeur//2-200, hauteur//2-25, largeur//2+200, hauteur//2+25)
    fltk.rectangle(largeur//2-200, hauteur//2+40, largeur//2+200, hauteur//2+90)
    fltk.texte(largeur//2, hauteur//2-65, 'Jouer', ancrage='center')
    fltk.texte(largeur//2, hauteur//2, 'Parametre', ancrage='center')
    fltk.texte(largeur//2, hauteur//2+65, 'Quitter', ancrage='center')
    while True:
        ev = fltk.donne_ev()
        tev = fltk.type_ev(ev)
        if tev == 'ClicGauche':
            if ((largeur//2-200)<fltk.abscisse(ev)<(largeur//2+200)) and ((hauteur//2-90)<fltk.ordonnee(ev)<(hauteur//2-40)):
                n = 1
                break
            if ((largeur//2-200)<fltk.abscisse(ev)<(largeur//2+200)) and ((hauteur//2-25)<fltk.ordonnee(ev)<(hauteur//2+25)):
                n = 2
                break
            if ((largeur//2-200)<fltk.abscisse(ev)<(largeur//2+200)) and ((hauteur//2+40)<fltk.ordonnee(ev)<(hauteur//2+90)):
                fltk.ferme_fenetre()
        elif tev == 'Quitte':
            fltk.ferme_fenetre()
        else:  
            pass
        fltk.mise_a_jour()
    fltk.efface_tout()
    return n, lst


def resolution(largeur, hauteur):
    fltk.rectangle(largeur//2-200, hauteur//2-60, largeur//2+200, hauteur//2-10)
    fltk.rectangle(largeur//2-200, hauteur//2+10, largeur//2+200, hauteur//2+60)
    fltk.rectangle(largeur-150, hauteur-65, largeur-20, hauteur-15)
    fltk.texte(largeur//2, 2, 'Taille de la fenetre', ancrage='n')
    fltk.texte(largeur//2, hauteur//2-35, '800/600', ancrage='center')
    fltk.texte(largeur//2, hauteur//2+35, '1920/1200', ancrage='center')
    fltk.texte(largeur-85, hauteur-40, 'Retour', ancrage='center')
    while True:
        ev = fltk.donne_ev()
        tev = fltk.type_ev(ev)
        if tev == 'ClicGauche':
            if ((largeur//2-200)<fltk.abscisse(ev)<(largeur//2+200)) and ((hauteur//2-60)<fltk.ordonnee(ev)<(hauteur//2-10)):
                lst = [800, 600]
                n = 2
                break
            if ((largeur//2-200)<fltk.abscisse(ev)<(largeur//2+200)) and ((hauteur//2-10)<fltk.ordonnee(ev)<(hauteur//2+60)):
                lst = [1920, 1200]
                fltk.ferme_fenetre()
                fltk.cree_fenetre(largeur, hauteur)
                n = 2
                break
            if ((largeur-150)<fltk.abscisse(ev)<(largeur-20)) and ((hauteur-65)<fltk.ordonnee(ev)<(hauteur-15)):
                lst = []
                n = 0
                break
        elif tev == 'Quitte':
            fltk.ferme_fenetre()
        else:  
            lst = [largeur, hauteur]
            pass
        fltk.mise_a_jour()
    fltk.efface_tout()
    return n, lst


def txt_para(largeur, hauteur, a, b, c, d):
    fltk.efface_tout()
    fltk.rectangle(largeur//2-200, hauteur//2-65, largeur//2+200, hauteur//2-115)
    fltk.rectangle(largeur//2-200, hauteur//2-55, largeur//2+200, hauteur//2-5)
    fltk.rectangle(largeur//2-200, hauteur//2+5, largeur//2+200, hauteur//2+55)
    fltk.rectangle(largeur//2-200, hauteur//2+115, largeur//2+200, hauteur//2+65)
    fltk.rectangle(largeur//2-200, hauteur//2+175, largeur//2+200, hauteur//2+125)
    fltk.rectangle(largeur-150, hauteur-65, largeur-20, hauteur-15)
    fltk.texte(2, hauteur//2-90, 'Adversaire :', ancrage='w')
    fltk.texte(largeur//2, hauteur//2-90, f'{adversaire[a]}', ancrage='center')
    fltk.texte(2, hauteur//2-30, '1er a jouer :', ancrage='w')
    fltk.texte(largeur//2, hauteur//2-30, f'{quicommence[b]}', ancrage='center')
    fltk.texte(2, hauteur//2+30, 'version :', ancrage='w')
    fltk.texte(largeur//2, hauteur//2+30, f'{variante[c]}', ancrage='center')
    fltk.texte(2, hauteur//2+90, 'mode :', ancrage='w')
    fltk.texte(largeur//2, hauteur//2+90, f'{mode[d]}', ancrage='center')
    fltk.texte(largeur//2, hauteur//2+150, 'Valide', ancrage='center')
    fltk.texte(largeur-85, hauteur-40, 'Retour', ancrage='center')


def parametre_du_jeu(largeur, hauteur):
    a, b, c, d = 0, 0, 0, 0
    txt_para(largeur, hauteur, a, b, c, d)
    while True:
        ev = fltk.donne_ev()
        tev = fltk.type_ev(ev)
        if tev == 'ClicGauche':
            if ((largeur//2-200)<fltk.abscisse(ev)<(largeur//2+200)) and ((hauteur//2-115)<fltk.ordonnee(ev)<(hauteur//2-65)):
                a += 1
            if ((largeur//2-200)<fltk.abscisse(ev)<(largeur//2+200)) and ((hauteur//2-55)<fltk.ordonnee(ev)<(hauteur//2-5)):
                b += 1
            if ((largeur//2-200)<fltk.abscisse(ev)<(largeur//2+200)) and ((hauteur//2+5)<fltk.ordonnee(ev)<(hauteur//2+55)):
                c += 1
            if ((largeur//2-200)<fltk.abscisse(ev)<(largeur//2+200)) and ((hauteur//2+65)<fltk.ordonnee(ev)<(hauteur//2+115)):
                d += 1
            if ((largeur//2-200)<fltk.abscisse(ev)<(largeur//2+200)) and ((hauteur//2+125)<fltk.ordonnee(ev)<(hauteur//2+175)):
                n = 5
                break
            if ((largeur-150)<fltk.abscisse(ev)<(largeur-20)) and ((hauteur-65)<fltk.ordonnee(ev)<(hauteur-15)):
                lst = []
                n = 0
                break
        elif tev == 'Quitte':
            fltk.ferme_fenetre()
        else:  
            pass
        a, b, c, d = a%3, b%2, c%3, d%2
        txt_para(largeur, hauteur, a, b, c, d)
        fltk.mise_a_jour()
    if c == 2 and n == 5:
        n = 3
    lst = [a, b, c, d]
    fltk.efface_tout()
    return n, lst


def nbcolonne(largeur, hauteur):
    fltk.texte(largeur//2, 20, 'Choisit le nombre de collones', ancrage='center')
    fltk.rectangle(largeur//2-200, hauteur//2-25, largeur//2+200, hauteur//2+25)
    fltk.rectangle(largeur-150, hauteur-65, largeur-20, hauteur-15)
    fltk.texte(largeur-85, hauteur-40, 'Retour', ancrage='center')
    fltk.texte(largeur//2, hauteur//2, 'choisit un chiffre', tag='press', ancrage='center')
    lst = []
    while True:
        ev = fltk.donne_ev()
        tev = fltk.type_ev(ev)
        if tev == 'Touche':
            if fltk.touche(ev) in persocol:
                fltk.efface('press')
                fltk.texte(largeur//2, hauteur//2, f'{fltk.touche(ev)}', tag='press', ancrage='center')
                lst = [fltk.touche(ev)]
        if len(lst) == 1:
            fltk.rectangle(largeur//2-200, hauteur//2+115, largeur//2+200, hauteur//2+65)
            fltk.texte(largeur//2, hauteur//2+90, 'valide', ancrage='center')
        if tev == 'ClicGauche':                
            if ((largeur//2-200)<fltk.abscisse(ev)<(largeur//2+200)) and ((hauteur//2+65)<fltk.ordonnee(ev)<(hauteur//2+115)) and len(lst)==1:
                n = 4
                break
            if ((largeur-150)<fltk.abscisse(ev)<(largeur-20)) and ((hauteur-65)<fltk.ordonnee(ev)<(hauteur-15)):
                lst = []
                n = 1
                break

        elif tev == 'Quitte':
            fltk.ferme_fenetre()
        else:  
            pass
        fltk.mise_a_jour()
    fltk.efface_tout()
    return n, lst


def nbelemparcol(largeur, hauteur, lst):
    fltk.rectangle(largeur//2-200, hauteur//2-25, largeur//2+200, hauteur//2+25)
    fltk.rectangle(largeur-150, hauteur-65, largeur-20, hauteur-15)
    fltk.texte(largeur-85, hauteur-40, 'Retour', ancrage='center')
    fltk.texte(largeur//2, hauteur//2, 'Choisit un nombre', tag='press', ancrage='center')
    listedujeu = []
    nbchoisit = 0
    n = 0
    while len(listedujeu) < int(lst[0]):
        fltk.texte(largeur//2, 20, f"Combien d'allumettes veux-tu sur la colonne {len(listedujeu)+1}", ancrage='center', tag='i')
        ev = fltk.donne_ev()
        tev = fltk.type_ev(ev)
        if tev == 'Touche':
            if fltk.touche(ev) in persocol or fltk.touche(ev) == '0':
                if nbchoisit == 0:
                    nbchoisit = int(fltk.touche(ev))
                elif nbchoisit<5 or (fltk.touche(ev)=='0'and nbchoisit==5):
                    nbchoisit = nbchoisit*10+int(fltk.touche(ev))  
                fltk.efface('press')
                fltk.texte(largeur//2, hauteur//2, f'{nbchoisit}', tag='press', ancrage='center')
            if fltk.touche(ev) == 'BackSpace':
                if nbchoisit < 10:
                    nbchoisit = 0
                else:
                    nbchoisit = (nbchoisit-nbchoisit%10)//10
                fltk.efface('press')
                fltk.texte(largeur//2, hauteur//2, f'{nbchoisit}', tag='press', ancrage='center')
        if nbchoisit != 0:
            fltk.efface('val')
            fltk.rectangle(largeur//2-200, hauteur//2+115, largeur//2+200, hauteur//2+65, tag='rect')
            fltk.texte(largeur//2, hauteur//2+90, 'valide', ancrage='center', tag='val')
        else:
            fltk.efface('rect')
            fltk.efface('val')
        if tev == 'ClicGauche':                
            
            if ((largeur//2-200)<fltk.abscisse(ev)<(largeur//2+200)) and ((hauteur//2+65)<fltk.ordonnee(ev)<(hauteur//2+115)) and nbchoisit!=0:
                listedujeu.append(nbchoisit)
                nbchoisit = 0
                fltk.efface('i')
                fltk.efface('press')
                fltk.texte(largeur//2, hauteur//2, 'Choisit un nombre', tag='press', ancrage='center')
            if ((largeur-150)<fltk.abscisse(ev)<(largeur-20)) and ((hauteur-65)<fltk.ordonnee(ev)<(hauteur-15)):
                lst = []
                n = 3
                break
        elif tev == 'Quitte':
            fltk.ferme_fenetre()
        else:  
            pass
        fltk.mise_a_jour()
    if len(listedujeu) == int(lst[0]):
        n = 5
    fltk.efface_tout()
    return n, listedujeu


def choixcouppossible(largeur, hauteur):
    lst = []
    fltk.rectangle(largeur//2-200, hauteur//2-90, largeur//2+200, hauteur//2-40)
    fltk.rectangle(largeur//2-200, hauteur//2-25, largeur//2+200, hauteur//2+25)
    fltk.rectangle(largeur//2-200, hauteur//2+40, largeur//2+200, hauteur//2+90)
    fltk.rectangle(largeur-150, hauteur-65, largeur-20, hauteur-15)
    fltk.texte(largeur//2, 2, 'Coups possibles', ancrage='n')
    fltk.texte(largeur//2, hauteur//2-65, '[1, 2, 3] / Nim', ancrage='center')
    fltk.texte(largeur//2, hauteur//2, '[1, ..., n] / Marienbad', ancrage='center')
    fltk.texte(largeur//2, hauteur//2+65, 'A choisir', ancrage='center')
    fltk.texte(largeur-85, hauteur-40, 'Retour', ancrage='center')
    while True:
        ev = fltk.donne_ev()
        tev = fltk.type_ev(ev)
        if tev == 'ClicGauche':
            if ((largeur//2-200)<fltk.abscisse(ev)<(largeur//2+200)) and ((hauteur//2-90)<fltk.ordonnee(ev)<(hauteur//2-40)):
                lst = [1, 2, 3]
                n = 7
                break
            if ((largeur//2-200)<fltk.abscisse(ev)<(largeur//2+200)) and ((hauteur//2-25)<fltk.ordonnee(ev)<(hauteur//2+25)):
                lst = [0]
                n = 7
                break
            if ((largeur//2-200)<fltk.abscisse(ev)<(largeur//2+200)) and ((hauteur//2+40)<fltk.ordonnee(ev)<(hauteur//2+90)):
                n = 6
                break
            if ((largeur-150)<fltk.abscisse(ev)<(largeur-20)) and ((hauteur-65)<fltk.ordonnee(ev)<(hauteur-15)):
                lst = []
                n = 1
                break
        elif tev == 'Quitte':
            fltk.ferme_fenetre()
        else:  
            pass
        fltk.mise_a_jour()
    fltk.efface_tout()
    return n, lst


def coupperso(largeur, hauteur, lin):
    fltk.rectangle(largeur//2-200, hauteur//2-25, largeur//2+200, hauteur//2+25)
    fltk.rectangle(largeur-150, hauteur-65, largeur-20, hauteur-15)
    fltk.texte(largeur-85, hauteur-40, 'Retour', ancrage='center')
    fltk.texte(largeur//2, 20, 'Choisit un des coups possibles (max 15 differents)', ancrage='center')
    fltk.texte(largeur//2, hauteur//2, 'choisit un chiffre', tag='press', ancrage='center')  
    coupmax = 1
    for e in lin:
        if e > coupmax:
            coupmax = e
    lstcoup = [1]
    nbchoisit = 0
    n = 7
    while True:
        ev = fltk.donne_ev()
        tev = fltk.type_ev(ev)
        fltk.texte(largeur//2, 60, f'{lstcoup}', tag='coup', ancrage='center')
        if tev == 'Touche':
            if fltk.touche(ev) in persocol or fltk.touche(ev) == '0':
               if nbchoisit == 0:
                   nbchoisit = int(fltk.touche(ev))
               elif (nbchoisit<5 or (fltk.touche(ev)=='0'and nbchoisit==5)) and nbchoisit*10+int(fltk.touche(ev))<=coupmax:
                   nbchoisit = nbchoisit*10+int(fltk.touche(ev))  
               fltk.efface('press')
               fltk.texte(largeur//2, hauteur//2, f'{nbchoisit}', tag='press', ancrage='center')
            if fltk.touche(ev) == 'BackSpace':
               if nbchoisit < 10:
                   nbchoisit = 0
               else:
                   nbchoisit = (nbchoisit-nbchoisit%10)//10
               fltk.efface('press')
               fltk.texte(largeur//2, hauteur//2, f'{nbchoisit}', tag='press', ancrage='center')
        if nbchoisit not in lstcoup and nbchoisit != 0:
            fltk.rectangle(largeur//2-200, hauteur//2+85, largeur//2+200, hauteur//2+35, tag='rect')
            fltk.texte(largeur//2, hauteur//2+60, 'Ajouter', ancrage='center', tag='ajout')
        else:
            fltk.efface('rect')
            fltk.efface('ajout')
        if len(lstcoup) > 1:
            fltk.rectangle(largeur//2-200, hauteur//2+145, largeur//2+200, hauteur//2+95)
            fltk.texte(largeur//2, hauteur//2+120, 'valide', ancrage='center')
        if tev == 'ClicGauche':
            if ((largeur//2-200)<fltk.abscisse(ev)<(largeur//2+200)) and ((hauteur//2+35)<fltk.ordonnee(ev)<(hauteur//2+85)) and nbchoisit not in lstcoup and nbchoisit!=0:
                lstcoup.append(nbchoisit)
                fltk.efface('coup')
                nbchoisit = 0
                fltk.efface('press')
                fltk.texte(largeur//2, hauteur//2, f'{nbchoisit}', tag='press', ancrage='center')
            if ((largeur//2-200)<fltk.abscisse(ev)<(largeur//2+200)) and ((hauteur//2+95)<fltk.ordonnee(ev)<(hauteur//2+145)) and len(lstcoup)>1:
                n = 7
                break
            if ((largeur-150)<fltk.abscisse(ev)<(largeur-20)) and ((hauteur-65)<fltk.ordonnee(ev)<(hauteur-15)):
                lstcoup = []
                n = 5
                break
        elif tev == 'Quitte':
            fltk.ferme_fenetre()
        else:  
            pass
        fltk.mise_a_jour()
    fltk.efface_tout()
    return n, lstcoup


def menu(n, lst, largeur, hauteur, lin):
    if n == 0:
        return menu_de_depart(largeur, hauteur)
    if n == 1:
        return parametre_du_jeu(largeur, hauteur)
    if n == 2:
        return resolution(largeur, hauteur)
    if n == 3:
        return nbcolonne(largeur, hauteur)
    if n == 4:
        return nbelemparcol(largeur, hauteur, lst)
    if n == 5:
        return choixcouppossible(largeur, hauteur)
    if n == 6:
        return coupperso(largeur, hauteur, lin)


def objet(largeur, hauteur, liste_de_jeu):
    taille_ligne = hauteur // (len(liste_de_jeu)+2)
    taille_col = largeur//50
    for i in range(len(liste_de_jeu)):
        for j in range(len(liste_de_jeu[i])):
            fltk.rectangle(taille_col*j+5, taille_ligne*(i+1)+5, taille_col*(j+1)-5, taille_ligne*(i+2)-5, remplissage='brown')
    return


def selection_baton(largeur, hauteur, liste_de_jeu, abscisse, ordonnee):
    taille_ligne = hauteur // (len(liste_de_jeu)+2)
    taille_col = largeur//50
    for i in range(len(liste_de_jeu)):
        for j in range(len(liste_de_jeu[i])):
            ax, bx, ay, by = taille_col*j, taille_col*(j+1), taille_ligne*(i+1), taille_ligne*(i+2)
            if ax<abscisse<bx and ay<ordonnee<by:
                return True, [ay, by], i, j
    return False, [ay, by], i, j


def partie(largeur, hauteur, liste_de_jeu, adversaire, m, variante, mode, lst_coup):
    taille_ligne = hauteur // (len(liste_de_jeu)+2)
    taille_col = largeur//50
    lst_col = []
    col = 0
    for i in range(len(liste_de_jeu)):
        lst_col.append(i+1)
    while fin_de_manche(liste_de_jeu):
        batons_choisit = 0
        lst_coord_ord = []
        lst_baton = []
        lst_col = verif_col(liste_de_jeu, lst_col)
        while True:
            if adversaire == 1 and m == 1:
                batons_choisit, col = choix_bot(1, variante+1, mode+1, liste_de_jeu, lst_col)
                liste_de_jeu[i] = retire_batons(batons_choisit, liste_de_jeu[col-1])
                break
            elif adversaire == 2 and m == 1:
                batons_choisit, col = choix_bot(2, variante+1, mode+1, liste_de_jeu, lst_col)
                liste_de_jeu[i] = retire_batons(batons_choisit, liste_de_jeu[col-1])
                break
            fltk.texte(largeur//2 , 50, 'Au tour du joueur ' + str(m+1), ancrage='center')
            fltk.texte(largeur//2, 100, 'Cliquez sur les allumettes que vous voulez prendre.', ancrage='center')
            objet(largeur, hauteur, liste_de_jeu)
            ev = fltk.donne_ev()
            tev = fltk.type_ev(ev)
            if batons_choisit in lst_coup:
                fltk.rectangle(largeur-145, hauteur-60, largeur-15, hauteur-10, tag='rect')
                fltk.texte(largeur-80, hauteur-35, 'Valide', ancrage='center', tag='val')
            else:
                fltk.efface('rect')
                fltk.efface('val')
            if len(lst_baton)!=0:
                for loop in range(len(lst_baton)):
                    i, j = lst_baton[loop]
                    col = j
                    fltk.rectangle(taille_col*j, taille_ligne*(i+1), taille_col*(j+1), taille_ligne*(i+2), couleur='red')
            if tev == 'ClicGauche':
                abscisse, ordonnee = fltk.abscisse(ev), fltk.ordonnee(ev)
                validation, ordo , i, j = selection_baton(largeur, hauteur, liste_de_jeu, abscisse, ordonnee)
                if validation and (i, j) not in lst_baton and j != col:
                    lst_coord_ord = ordo
                    batons_choisit += 1
                    lst_baton.append((i, j))
                elif (i, j) in lst_baton:
                    batons_choisit -= 1
                    lst_baton.remove((i, j))
                    if batons_choisit == 0:
                        lst_coord_ord = []
                if ((largeur-145)<fltk.abscisse(ev)<(largeur-15)) and ((hauteur-60)<fltk.ordonnee(ev)<(hauteur-10)) and batons_choisit in lst_coup:
                    i, j = lst_baton[0]
                    liste_de_jeu[i] = retire_batons(batons_choisit, liste_de_jeu[i])
                    break
            elif tev == 'Quitte':
                fltk.ferme_fenetre()
            else:  
                pass
            fltk.mise_a_jour()
            fltk.efface_tout()
        m = joueur(m+1)
    return

