from fltk import*
from fonctions import*
from gui import*
from time import*


# Constantes 
coord1 = None 

x = 800 
y = 800
partie = True

lst = ["right","left","up","down"]

cree_fenetre(x,y)
# menu principal
while True : 
    game = False 
    menu1 = menu_depart(x,y)
    
    
# configuration du jeu
    
    while menu1 : 
        suiv = 0
        # difficulté de la map
        if suiv == 0 :
            suiv,lstmap = style_fichier(x,y)
        # choix de la map
        if suiv == 1 :
            nmap,suiv = choix_style(x,y,lstmap)
        # chargement de la map
        if suiv == 2 : 
            fich = lstmap[nmap]
            plat = plateau(fich) 
            coorde = indice(plat,"S") 
            touffe = indice(plat,"G")
            jeupossible = True
            game = True 
            break
        if suiv < 0 :
            break



    while not menu1 : 
        # parametres graphique
        para = parametre (x,y) 
        if para == 3 : 
            newres = resolution(x,y)
            x,y = newres[0],newres[1]
            ferme_fenetre()
            cree_fenetre(x,y)
        #map personnalisée
        if para == 4 : 
            fich = map_perso(x,y)
            plat = plateau(fich) 
            coorde = indice(plat,"S") 
            touffe = indice(plat,"G")
            jeupossible = True
            game = True 
            break

    while game : 
        if jeupossible : 
            #affichage du jeu 
            coup = jeu(x,y,plat)
            #maj du jeu
            plat,coorde = refresh(plat,coorde,coup,touffe)
            #fonction victoire
            findejeu = victoire(plat)
          
            #Si le joueur gagne 
            if findejeu : 
                rejouer = menu_victoire(x,y,plat)
                #Retour au menu principal 
                if rejouer : 
                    break
            #regarde si le jeu n'est pas bloqué 
            jeupossible =  analyse(plat,coorde,touffe)
        #si le jeu est bloqué
        else : 
            rejouer = menu_bloquage(x,y,plat)
            #retour au menu principal 
            if rejouer : 
                 break 

    
 
   
        
    