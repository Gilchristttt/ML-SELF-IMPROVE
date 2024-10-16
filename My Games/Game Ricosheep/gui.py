from time import*
from fltk import*
from fonctions import*
def jeu(largeur,hauteur,plateau):
    case = mesure_grille(largeur,hauteur,len(plateau),len(plateau[0])) # taille de mes cases
    indcol = 0
    efface_tout()
    
    while True : 
        
        for i in range (len(plateau)) : 
            indligne  = 0 
            for k in plateau[i] :
                rectangle(indligne,indcol, indligne + case, indcol+ case )
                if k == "B" : 
                    image(indligne+70 ,indcol+70,"bush.png")
                if k == "G" : 
                    image(indligne + 70,indcol+70,"grass.png")
                if k =="S":
                    image(indligne + 70,indcol+70,"sheep.png")    
                if k == "SG":
                    image(indligne + 70,indcol+70,"sheep_grass.png")

                indligne += case 
            indcol += case
        while True:
            ev = donne_ev()
            tev= type_ev(ev)

            if tev == "Touche" :
                if touche(ev) == "Right" : 
                    n = 0
                    break
                if touche(ev) == "Left" : 
                    n = 1
                    break
                if touche(ev) == "Up" : 
                    n = 2
                    break
                if touche(ev) == "Down" : 
                    n = 3
                    break
            elif tev == 'Quitte':
                ferme_fenetre()
            else:  
                pass
            mise_a_jour()


        return n

def menu_bloquage(largeur,hauteur,plateau) : 
    case = mesure_grille(largeur,hauteur,len(plateau),len(plateau[0])) # taille de mes cases
    indcol = 0
    # Affichage
    while True : 
        efface_tout()
            
        for i in range (len(plateau)) : 
            indligne  = 0 
            for k in plateau[i] :
                rectangle(indligne,indcol, indligne + case, indcol+ case )
                if k == "B" : 
                    image(indligne+70 ,indcol+70,"bush.png")
                elif k == "G" : 
                    image(indligne + 70,indcol+70,"grass.png")
                elif k =="S":
                    image(indligne + 70,indcol+70,"sheep.png")    
                elif k == "SG":
                    image(indligne + 70,indcol+70,"sheep_grass.png")

                indligne += case 
            indcol += case
        texte(largeur//2, 2, 'Tous les moutons sont bloqués, Vous avez perdu la partie', ancrage='center')
        mise_a_jour()
        sleep(3)

        efface_tout()
        
        rectangle(largeur//2-200, hauteur//2-25, largeur//2+200, hauteur//2+25,remplissage="yellow")
        rectangle(largeur//2-200, hauteur//2+40, largeur//2+200, hauteur//2+90,remplissage="red")
        texte(largeur//2, 2, 'Vous avez perdu la partie, voulez-vous rejouer ?', ancrage='n')
        texte(largeur//2, hauteur//2, 'Rejouer', ancrage='center')
        texte(largeur//2, hauteur//2+65, 'Quitter', ancrage='center')
        while True : 
            ev = donne_ev()
            tev = type_ev(ev)
            if tev == 'ClicGauche':
                if ((largeur//2-200)<abscisse(ev)<(largeur//2+200)) and ((hauteur//2-25)<ordonnee(ev)<(hauteur//2+25)):
                    return True
                if ((largeur//2-200)<abscisse(ev)<(largeur//2+200)) and ((hauteur//2+40)<ordonnee(ev)<(hauteur//2+90)):
                    ferme_fenetre()
            elif tev == 'Quitte':
                ferme_fenetre()
            
            mise_a_jour() 

def menu_victoire(largeur,hauteur,plateau) : 
    case = mesure_grille(largeur,hauteur,len(plateau),len(plateau[0])) 
    indcol = 0
    while True : 
        efface_tout()
            
        for i in range (len(plateau)) : 
            indligne  = 0 
            for k in plateau[i] :
                rectangle(indligne,indcol, indligne + case, indcol+ case )
                if k == "B" : 
                    image(indligne+70 ,indcol+70,"bush.png")
                elif k == "G" : 
                    image(indligne + 70,indcol+70,"grass.png")
                elif k =="S":
                    image(indligne + 70,indcol+70,"sheep.png")    
                elif k == "SG":
                    image(indligne + 70,indcol+70,"sheep_grass.png")

                indligne += case 
            indcol += case
        rectangle(largeur//2-200,hauteur//2-25,largeur//2+200,hauteur//2+25,remplissage='white')
        texte(largeur//2, hauteur//2, 'You win', ancrage='center',couleur = "green",police = "Courier")
        mise_a_jour()
        sleep(3)
        efface_tout()

        rectangle(largeur//2-200, hauteur//2-25, largeur//2+200, hauteur//2+25,remplissage="yellow")
        rectangle(largeur//2-200, hauteur//2+40, largeur//2+200, hauteur//2+90,remplissage="red")
        texte(largeur//2, 2, 'Vous avez gagner la partie, voulez-vous rejouer ?', ancrage='n')
        texte(largeur//2, hauteur//2, 'Rejouer', ancrage='center')
        texte(largeur//2, hauteur//2+65, 'Quitter', ancrage='center')
        while True : 
            ev = donne_ev()
            tev = type_ev(ev)
            if tev == 'ClicGauche':
                if ((largeur//2-200)<abscisse(ev)<(largeur//2+200)) and ((hauteur//2-25)<ordonnee(ev)<(hauteur//2+25)):
                    return True
                if ((largeur//2-200)<abscisse(ev)<(largeur//2+200)) and ((hauteur//2+40)<ordonnee(ev)<(hauteur//2+90)):
                    ferme_fenetre()
            elif tev == 'Quitte':
                ferme_fenetre()
            
            mise_a_jour() 

def menu_depart(largeur,hauteur):
    """ 
    Fonction graphique permettant d'initialiser la fénetre de jeu.
    paramètre:
     entrés : 
        largeur == int
        hauteur == int
     return 
         n == int
         lst == list
    
    """
    while True : 
        efface_tout()
        lst=[]
        rectangle(largeur//2-200, hauteur//2-90, largeur//2+200, hauteur//2-40,remplissage="red")
        rectangle(largeur//2-200, hauteur//2-25, largeur//2+200, hauteur//2+25,remplissage="yellow")
        rectangle(largeur//2-200, hauteur//2+40, largeur//2+200, hauteur//2+90,remplissage="red")
        texte(largeur//2, hauteur//5, 'WELCOME', ancrage='center')
        image(largeur//2,hauteur//3,"sheep.png") 
        texte(largeur//2, hauteur//2-65, 'Jouer', ancrage='center')
        texte(largeur//2, hauteur//2, 'Parametre', ancrage='center')
        texte(largeur//2, hauteur//2+65, 'Quitter', ancrage='center')
        while True:
            ev = donne_ev()
            tev = type_ev(ev)
            if tev == 'ClicGauche':
                if ((largeur//2-200)<abscisse(ev)<(largeur//2+200)) and ((hauteur//2-90)<ordonnee(ev)<(hauteur//2-40)):
                    return True
                if ((largeur//2-200)<abscisse(ev)<(largeur//2+200)) and ((hauteur//2-25)<ordonnee(ev)<(hauteur//2+25)):
                    return False
                if ((largeur//2-200)<abscisse(ev)<(largeur//2+200)) and ((hauteur//2+40)<ordonnee(ev)<(hauteur//2+90)):
                    ferme_fenetre()
            elif tev == 'Quitte':
                ferme_fenetre()
            
            mise_a_jour()
    
def parametre(largeur, hauteur):
    while True : 
        efface_tout()
        lst =[]
        rectangle(largeur//2-200, hauteur//2-90, largeur//2+200, hauteur//2-40,remplissage="red")
        rectangle(largeur//2-200, hauteur//2-25, largeur//2+200, hauteur//2+25,remplissage="yellow")
        rectangle(largeur//2-200, hauteur//2+40, largeur//2+200, hauteur//2+90,remplissage="green")
        rectangle(largeur-150, hauteur-65, largeur-20, hauteur-15)
        texte(largeur//2, hauteur//2-65, 'Modifier la fenetre', ancrage='center')
        texte(largeur//2, hauteur//2, 'Importer un plateau', ancrage='center')
        texte(largeur//2, hauteur//2+65, 'Quitter', ancrage='center')
        texte(largeur-85, hauteur-40, 'Retour', ancrage='center')
        while True:
            
            ev = donne_ev()
            tev = type_ev(ev)
            if tev == 'ClicGauche':
                if ((largeur//2-200)<abscisse(ev)<(largeur//2+200)) and ((hauteur//2-90)<ordonnee(ev)<(hauteur//2-40)):
                    n = 3
                    break
                if ((largeur//2-200)<abscisse(ev)<(largeur//2+200)) and ((hauteur//2-25)<ordonnee(ev)<(hauteur//2+25)):
                    n = 4
                    break
                if ((largeur//2-200)<abscisse(ev)<(largeur//2+200)) and ((hauteur//2+40)<ordonnee(ev)<(hauteur//2+90)):
                    ferme_fenetre()
                if ((largeur-150)<abscisse(ev)<(largeur-20)) and ((hauteur-65)<ordonnee(ev)<(hauteur-15)):
                    n = 0
                    break
                
            elif tev == 'Quitte':
                ferme_fenetre()
            else:  
                pass
            mise_a_jour()
        
        return n

def resolution(largeur, hauteur):

    while True : 
        efface_tout()
        lst =[]
        rectangle(largeur//2-200, hauteur//2-60, largeur//2+200, hauteur//2-10,remplissage="blue")
        rectangle(largeur//2-200, hauteur//2+10, largeur//2+200, hauteur//2+60,remplissage="red")
        rectangle(largeur-150, hauteur-65, largeur-20, hauteur-15)
        texte(largeur//2, 2, 'Taille de la fenetre', ancrage='n')
        texte(largeur//2, hauteur//2-35, '1500/1000', ancrage='center')
        texte(largeur//2, hauteur//2+35, '1000/1000', ancrage='center')
        texte(largeur-85, hauteur-40, 'Retour', ancrage='center')
        while True:
            
            ev = donne_ev()
            tev = type_ev(ev)
            if tev == 'ClicGauche':
                if ((largeur//2-200)<abscisse(ev)<(largeur//2+200)) and ((hauteur//2-60)<ordonnee(ev)<(hauteur//2-10)):
                    lst = [1500, 1000]
                    n = 2
                    break
                if ((largeur//2-200)<abscisse(ev)<(largeur//2+200)) and ((hauteur//2-10)<ordonnee(ev)<(hauteur//2+60)):
                    lst = [1000, 1000]
                    n = 2
                    break
                if ((largeur-150)<abscisse(ev)<(largeur-20)) and ((hauteur-65)<ordonnee(ev)<(hauteur-15)):
                    lst = []
                    n = 0
                    break
            elif tev == 'Quitte':
                ferme_fenetre()
            else:  
                lst = [largeur, hauteur]
                pass
            mise_a_jour()
        
        return  lst

def map_perso(largeur,hauteur) : 
    txt = ""
    while True : 
       efface_tout()
       rectangle(largeur//2-200, hauteur//2-90, largeur//2+200, hauteur//2-40,remplissage="white")
       texte(largeur//2, hauteur//2-65, 'Saisir le nom du fichier', ancrage='center')
       rectangle(largeur//2-200, hauteur//2-25, largeur//2+200, hauteur//2+25,remplissage="white")
       texte(largeur//2, hauteur//2, txt, ancrage='center')
       rectangle(largeur-150, hauteur-65, largeur-20, hauteur-15,remplissage="green" )
       texte(largeur-85, hauteur-40, 'Valider',couleur = "white",ancrage='center')
       
       while True : 
           ev = donne_ev()
           tev = type_ev(ev)
           if tev == 'Touche' : 
                if touche(ev)== "Caps_Lock"  or touche(ev)== "Shift_L": 
                   break
                if touche(ev)== "BackSpace" : 
                   txt = txt[:-1]
                   break
                elif touche(ev)== "period" : 
                    txt += "."
                    break
                else : 
                  txt += touche(ev)
                  break
           if tev == 'ClicGauche':
               if ((largeur-150)<abscisse(ev)<(largeur-20)) and ((hauteur-65)<ordonnee(ev)<(hauteur-15)): 
                   return txt

           elif tev == 'Quitte':
                ferme_fenetre()
           else:
                pass
           mise_a_jour()
        
           
           


def style_fichier(largeur, hauteur):
    while True : 
        efface_tout()
        lst=[]
        rectangle(largeur//2-200, hauteur//2-90, largeur//2+200, hauteur//2-40,remplissage="orange")
        rectangle(largeur//2-200, hauteur//2-25, largeur//2+200, hauteur//2+25,remplissage="red")
        rectangle(largeur//2-200, hauteur//2+40, largeur//2+200, hauteur//2+90,remplissage="blue")
        rectangle(largeur-150, hauteur-65, largeur-20, hauteur-15)
        texte(largeur//2, hauteur//2-65, 'Petite maps', ancrage='center')
        texte(largeur//2, hauteur//2, 'Moyennes maps', ancrage='center')
        texte(largeur//2, hauteur//2+65, 'Grandes maps', ancrage='center')
        texte(largeur-85, hauteur-40, 'Retour', ancrage='center')
        
        while True:
            ev = donne_ev()
            tev = type_ev(ev)
            if tev == 'ClicGauche':

                if ((largeur//2-200)<abscisse(ev)<(largeur//2+200)) and ((hauteur//2-90)<ordonnee(ev)<(hauteur//2-40)):
                    n = 1
                    lst = ["map1.txt","map2.txt","map3.txt"]
                    break

                if ((largeur//2-200)<abscisse(ev)<(largeur//2+200)) and ((hauteur//2-25)<ordonnee(ev)<(hauteur//2+25)):
                    n = 1
                    lst = ["wide2.txt","wide3.txt","wide4.txt"]
                    break
                    
                if ((largeur//2-200)<abscisse(ev)<(largeur//2+200)) and ((hauteur//2+40)<ordonnee(ev)<(hauteur//2+90)):
                    n = 1
                    lst=["big1.txt","big2.txt","big3.txt"]
                    break
                if ((largeur-150)<abscisse(ev)<(largeur-20)) and ((hauteur-65)<ordonnee(ev)<(hauteur-15)):
                    lst = []
                    n = -1
                    break
                    
            elif tev == 'Quitte':
                ferme_fenetre()
            else:
                pass
            mise_a_jour()
        efface_tout()
        return  n, lst

def choix_style(largeur, hauteur, style):
    while True :
        efface_tout()
     
        rectangle(largeur//2-200, hauteur//2-90, largeur//2+200, hauteur//2-40,remplissage="blue")
        rectangle(largeur//2-200, hauteur//2-25, largeur//2+200, hauteur//2+25)
        rectangle(largeur//2-200, hauteur//2+40, largeur//2+200, hauteur//2+90,remplissage="red")
        rectangle(largeur-150, hauteur-65, largeur-20, hauteur-15)
        texte(largeur//2, hauteur//2-65, style[0], ancrage='center')
        texte(largeur//2, hauteur//2, style[1], ancrage='center')   
        texte(largeur//2, hauteur//2+65, style[2], ancrage='center')
        texte(largeur-85, hauteur-40, 'Retour', ancrage='center')
        while True:
            ev = donne_ev()
            tev = type_ev(ev)
            if tev == 'ClicGauche':
                if ((largeur//2-200)<abscisse(ev)<(largeur//2+200)) and ((hauteur//2-90)<ordonnee(ev)<(hauteur//2-40)):
                    n = 0
                    suiv = 2
                    break
                if ((largeur//2-200)<abscisse(ev)<(largeur//2+200)) and ((hauteur//2-25)<ordonnee(ev)<(hauteur//2+25)):
                    n = 1
                    suiv = 2
                    break
                if ((largeur//2-200)<abscisse(ev)<(largeur//2+200)) and ((hauteur//2+40)<ordonnee(ev)<(hauteur//2+90)):
                    n = 2
                    suiv = 2
                    break
                if ((largeur-150)<abscisse(ev)<(largeur-20)) and ((hauteur-65)<ordonnee(ev)<(hauteur-15)):
                   
                    suiv = 0
                    n = 3
                    break
            elif tev == 'Quitte':
                ferme_fenetre()
            else:  
                pass
            mise_a_jour()
        efface_tout()
        return n,suiv