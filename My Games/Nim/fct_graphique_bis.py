import fltk


largeur = 800
hauteur = 600
 
    
def menu_de_depart():
    fltk.rectangle(largeur//2-200, hauteur//2-60, largeur//2+200, hauteur//2-10)
    fltk.rectangle(largeur//2-200, hauteur//2+10, largeur//2+200, hauteur//2+60)
    fltk.texte(largeur//2, hauteur//2-35, 'Jouer', ancrage='center')
    fltk.texte(largeur//2, hauteur//2+35, 'Quitter', ancrage='center')
    a = 0
    while True:
        ev = fltk.donne_ev()
        tev = fltk.type_ev(ev)
        if tev == 'ClicGauche':
            if ((largeur//2-200)<fltk.abscisse(ev)<(largeur//2+200)) and ((hauteur//2-60)<fltk.ordonnee(ev)<(hauteur//2-10)):
                a = 1
                break
            elif ((largeur//2-200)<fltk.abscisse(ev)<(largeur//2+200)) and ((hauteur//2+10)<fltk.ordonnee(ev)<(hauteur//2+60)):
                a = 2
                break
        elif tev == 'Quitte':
            a = 2
            break
        else:  
            pass
        fltk.mise_a_jour()
    fltk.efface_tout()
    return a

def menu(a, b, c):
    fltk.rectangle(largeur//2-200, hauteur//2-60, largeur//2+200, hauteur//2-10)
    fltk.rectangle(largeur//2-200, hauteur//2+10, largeur//2+200, hauteur//2+60)
    fltk.rectangle(largeur-145, hauteur-65, largeur-20, hauteur-15)
    fltk.texte(largeur//2, hauteur//2-35, f'{a}', ancrage='center')
    fltk.texte(largeur//2, hauteur//2+35, f'{b}', ancrage='center')
    fltk.texte((largeur/10)*9, (hauteur/15)*14, f'{c}', ancrage='center')
    n = 0
    while True:
        ev = fltk.donne_ev()
        tev = fltk.type_ev(ev)
        if tev == 'ClicGauche':
            if ((largeur//2-200)<fltk.abscisse(ev)<(largeur//2+200)) and ((hauteur//2-60)<fltk.ordonnee(ev)<(hauteur//2-10)):
                n = 1
                break
            elif ((largeur//2-200)<fltk.abscisse(ev)<(largeur//2+200)) and ((hauteur//2+10)<fltk.ordonnee(ev)<(hauteur//2+60)):
                n = 2
                break
            elif ((largeur-145)<fltk.abscisse(ev)<(largeur-20)) and ((hauteur-65)<fltk.ordonnee(ev)<(hauteur-15)):
                n = 3
                break
        elif tev == 'Quitte':
            break
        else:  
            pass
        fltk.mise_a_jour()
    fltk.efface_tout()
    return n

def menu_choix_adversaire():
    n = menu('Joueur', 'Ordi', 'Retour')
    return n 

def menu_choix_ordi():
    n = menu('Facile', 'Difficil', 'Retour')
    return n 

def menu_choix_joueur():
    n = menu('Joueur1', 'Joueur2', 'Retour')
    return n 

def menu_choix_jeu():
    n = menu('Nim', 'Marienbad', 'Retour')
    return n 

def menu_choix_mode():
    n = menu('Normal', 'Misere', 'Retour')
    return n 

def init():
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    a = menu_de_depart()
    while a != 2:
        b = menu_choix_adversaire()
        while b != 3:
            if b == 2:
                c = menu_choix_ordi()
            if c != 3:
                d = menu_choix_joueur()
                while d != 3:
                    e = menu_choix_jeu()
                    while e != 3:
                        f = menu_choix_mode()
                        while f != 3:
                            if f in [1, 2]:
                                break
                            f = menu_choix_mode()
                        if f in [1, 2]:
                            break
                        e = menu_choix_jeu()
                    if f in [1, 2]:
                        break
                    d = menu_choix_joueur()
                if b == 2:
                    if f in [1, 2]:
                        break   
                    c = menu_choix_ordi()
            if f in [1, 2]:
                break
            b = menu_choix_adversaire()
        if f in [1, 2]:
            break
        a = menu_de_depart()
    return a, b, c, d, e, f


def objet(col=1, lin=21):
    for i in range(col):
        for j in range(lin):
            fltk.rectangle(largeur/80+(largeur/30)*j,(hauteur/2)-50, (largeur+largeur)/80+(largeur/30)*j, (hauteur/2)+50, remplissage="beige")
            fltk.cercle(15+(largeur/30)*j, (hauteur/2)-55, largeur/100, remplissage="red")
    return
