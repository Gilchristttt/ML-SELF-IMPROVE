from fltk import*
import copy

def read(fich):
    """
    Fonction permettant de lire dans un fichier et de transformer les chaines de 
    caractères du fichier en liste de chaine de caractère.
    paramètres:
         entré: fichier
         return : liste

    >>> read("map2.txt")
    ['_B_BS', 'BB_S_', '_GBBS', '_BG__', '___BS']

    """
    fichier = open(fich,"r")
    read = fichier.readlines()
    plateau=[]
    for ligne in read:
        chaine= ligne.strip()
        plateau.append(chaine)
    fichier.close()
    return plateau
    
def plateau(fiche):
    """
    Fonction qui prend en paramètre un fichier (grille de jeu obtenue avec la fonction
    read(fiche) créer plus haut et remplace les "_" par None  et retourne une liste de cette grille.
    paramètres:
         entrée: fichier
         return : liste
    fiche="map2.txt"
    >>> plateau(fiche)
    [[None, 'B', None, 'B', 'S'], ['B', 'B', None, 'S', None], [None, 'G', 'B', 'B', 'S'],
    [None, 'B', 'G', None, None], [None, None, None, 'B', 'S']]

    """
    chaine = read(fiche)
    lst=[]
    for i in range(len(chaine)):
        lst.append([])
    a=0
    for elem in chaine:
        for i in range(len(elem)):
            if elem[i]=="_" : 
                lst[a].append(None)
                
            else:
                lst[a].append(elem[i])
        a+=1
    return lst 

def refresh(plateau,coord, nb,touffe) :
    """
    Fonction qui met à jour le plateau et les coordonées des moutons, ne renvoie pas de nouvelles liste
    mais modifie celles en paramètres.
    Paramètres  : 
     plateau,coord,touffe  = listes
     nb = int 
    Return : listes 
    
    plat = [['B', 'B', None, 'B', None], ['S', 'S', None, 'G', None]]
    coord = [(1,0),(1,1)]
    touffe = [(1,3)]
    >>> deplacement (plat,0,coord,touffe)
    [['B', 'B', None, 'B', None], [None, None, None, 'SG','S']],[(1,3),(1,4)]

    """
    lst = ["right","left","up","down"]
    plateau, coord = deplacement(plateau,lst[nb],coord,touffe)
    return plateau,coord

def coord(fiche):
    
    """
    Fonction qui prend en paramètre un fichier,( et fait appel à la fonction read(fiche))
    et récupère la position des moutons("S") par le biais de liste retourner par la fonction
    read(fiche).
    paramètres:
         entré: fichier
         return : liste
    fiche="map2.txt"
    >>> coord(fiche)
    [(0, 4), (1, 3), (2, 4), (4, 4)]
    """

    chaine = read(fiche)
    coord=[]
    for elem in chaine:
        for i in range(len(elem)):
            if elem[i]=="S" :
                    coord.append((chaine.index(elem),i))
                
     
    return coord

def indice_lst(plateau, liste = ["S","SG"]): 
    """
    Fonction qui return une liste de tuples qui correspondent aux indices des moutons dans le plateau.
    Paramètre : liste
    Return : liste
    plateau = [[None, 'B', None, 'B', 'S'], ['B', 'B', None, None, None], [None, 'SG', 'B', 'B', None], [None, 'B', 'G', None, 'S'], [None, None, 'S', 'B', None]]
    >>> indice_lst(plateau)
    [(0, 4), (2, 1), (3, 4), (4, 2)]


    """
    indice =[]
    for elem in plateau:
        for j in range(len(elem)):
            if elem[j] in liste : 
                ind=(plateau.index(elem),j)
                indice.append(ind)
    return indice

def indice(plateau, lettre): 
    """
    Fonction qui return une liste de tuples qui correspondent aux indices de la lettre dans le plateau.
    Paramètres : 
     plateau = liste
     lettre = str
    Return : 
     liste
    plateau  =[[None, None, None, 'G', None], [None, None, None, None, None], [None, None, None, None, None], ['B', 'B', None, None, None], ['S', 'S', None, None, None]]
    >>> indice(plateau,'S')
    [(4, 0), (4, 1)]

    """
    indice =[]
    for elem in plateau:
        for j in range(len(elem)):
            if elem[j] == lettre:
                ind=(plateau.index(elem),j)
                indice.append(ind)
    return indice

def mesure_grille(x,y,l,c) : 
    """
    x = x de la fenetre
    y = y de la fenetre  
    l =  nombre de lignes 
    c = nombre de colonnes
    La fonction me permet de déterminer la taille des cases pour n'importe quelle taille de fenetres et aussi n'importe quelle map.
    """
    cas1 = x // c -40
    cas2 = y// l -40
    taille = max(cas1,cas2)
    return taille
    
def deplacement(plat,mouvement,coord,touffe) : 
    """
    Fonction pour les déplacements des moutons qui renvoie deux nouvelles listes qui correspondent 
    au nouveau plateau et aux nouvelles coordonnées des moutons après le déplacement.
    Paramètres : 
       plat,coord,touffe = listes
       mouvement = str
    Return : 
        listes 
    
    plat = [['B', 'B', None, 'B', None], ['S', 'S', None, 'G', None]]
    coord = [(1,0),(1,1)]
    touffe = [(1,3)]
    >>> deplacement (plat,"right",coord,touffe)
    [['B', 'B', None, 'B', None], [None, None, None, 'SG','S']],[(1,3),(1,4)]
    
    """
    platc= copy.deepcopy(plat)
    coorde = copy.deepcopy(coord)
    if mouvement == "up":
        for i in coorde : 
            x = i[0]
            y = i[1]
            if x > 0 :
                if (platc[x-1][y] == "B" or  platc[x-1][y] == "S" or platc[x-1][y] == "SG") : 
                    continue
                else :
                    temp = x-1
                    while(platc[temp][y] == None or platc[temp][y]== "G") and temp > 0  : 
                        temp-= 1 
                    if (temp,y) in touffe  and platc[temp][y]!= "SG" : 
                        platc[temp][y] = "SG"
                        if i in touffe  : 
                            platc[x][y] = "G"
                        else : 
                            platc[x][y]= None
                    
                    elif platc[temp][y]== None: 
                        platc[temp][y] = "S"
                        if i in touffe  :
                            platc[x][y] = "G"
                        else : 
                            platc[x][y]= None
                
                    else :
                        if (temp+1,y) in touffe : 
                            platc[temp+1][y] = "SG"
                        else : 
                            platc[temp+1][y] = "S"
                        if i in touffe  : 
                                platc[x][y] = "G"
                        else : 
                            platc[x][y]= None
    
    if mouvement == "down":
        coorde = coorde[::-1]
        for i in coorde : 
            x = i[0]
            y = i[1]
            if x < len(platc)-1 :
                if (platc[x+1][y] ==  "B" or platc[x+1][y] ==  "S" or platc[x+1][y] ==  "SG") : 
                    continue
                else :
                    temp = x+1
                    while temp < len(platc)-1 and (platc[temp][y] == None or platc[temp][y]== "G")  : 
                        temp+= 1 
                    if (temp,y) in touffe and platc[temp][y]!= "SG" : 
                        platc[temp][y] = "SG"
                        if i in touffe  :
                            platc[x][y] = "G"
                        else : 
                            platc[x][y]= None
                    elif platc[temp][y] == None : 
                        platc[temp][y] = "S"
                        if i in touffe  :
                            platc[x][y] = "G"
                        else : 
                            platc[x][y]= None
                
                    else :
                        if (temp-1,y) in touffe : 
                            platc[temp-1][y] = "SG"
                        else : 
                            platc[temp-1][y] = "S"
                        if i in touffe  : 
                                platc[x][y] = "G"
                        else : 
                            platc[x][y]= None
    if mouvement == "left":
        for i in coorde : 
            x = i[0]
            y = i[1]
            if y > 0 :
                if (platc[x][y-1] == "B" or platc[x][y-1] == "S" or platc[x][y-1] == "SG" ):
                    continue
                else :
                    temp = y-1
                    while(platc[x][temp] == None or platc[x][temp]== "G") and temp > 0  : 
                        temp-= 1 
                    
                    if (x,temp) in touffe and platc[x][temp]!= "SG": 
                        platc[x][temp] = "SG"
                        if i in touffe  :
                            platc[x][y] = "G"
                        else : 
                            platc[x][y]= None
                    
                    elif platc[x][temp] == None: 
                        platc[x][temp] = "S"
                        if i in touffe  :
                            platc[x][y] = "G"
                        else : 
                            platc[x][y]= None
                    
                    else : 
                
                        if (x,temp+1) in touffe : 
                            platc[x][temp+1] = "SG"
                        else : 
                            platc[x][temp+1] = "S"
                        if i in touffe  : 
                                platc[x][y] = "G"
                        else : 
                            platc[x][y]= None
        
    if mouvement == "right":
        coorde = coorde[::-1]
        for i in coorde : 
            x = i[0]
            y = i[1]
            if y < len(platc[0])-1 : 
                if (platc[x][y+1] == "B" or platc[x][y+1] == "S"  or platc[x][y+1] == "SG" ) : 
                    continue
                else :
                    temp = y+1
                    while (platc[x][temp] == None or platc[x][temp]== "G") and  temp < len(platc[0])-1 : 
                        temp+= 1 
                    if (x,temp) in touffe and platc[x][temp]!= "SG": 
                        platc[x][temp] = "SG"
                        if i in touffe  :
                            platc[x][y] = "G"
                        else : 
                            platc[x][y]= None
                    elif platc[x][temp] == None : 
                        platc[x][temp] = "S"
                        if i in touffe  :
                            platc[x][y] = "G"
                        else : 
                            platc[x][y]= None
                
                    else : 
                        if (x,temp-1) in touffe : 
                           platc[x][temp-1] = "SG"
                        else : 
                           platc[x][temp-1] = "S"
                        if i in touffe  : 
                            platc[x][y] = "G"
                        else : 
                            platc[x][y]= None
    moutons = indice_lst(platc)
    return platc,moutons          
 
def victoire(plateau): 
    """
    Fonction qui détermine la victoire, si une case dans le plateau est une touffe d'herbe return False.
    Sinon return True 
    Paramètre :  Liste
    Return : Booléen 
    plateau = [['S', 'G', 'B', 'B', None], [None, 'B', 'SG', None, None]]
    plateau2 = [None, 'B ', 'B', 'B', None], [None, 'B', 'SG', None, None]
    >>> victoire(plateau)
    False
    >>> victoire(plateau2)
    True
    """
    for col in plateau : 
        for case in col : 
            if case == "G" : 
                return False 
    return True

def analyse(plat,coord,touffe) : 
    """
    Fonction qui vérifie le joueur peut jouer un coup au prochain tour
    Paramètres : 
     plat = liste
     coord = liste 
     touffe = liste
    Return : Booléen
    plat = [['B', 'B', None, 'B', None], ['S', 'S', 'B', None, None]]
    coord = [(1,0),(1,1)]
    touffe = []
    >>> analyse(plat,coord,touffe)
    False

    """
    lst = [0,1,2,3]
    cmpt = 0  
    for i in lst : 
        temp = coup_possible(plat,i,coord,touffe)
        if not temp : 
            cmpt += 1 
    if cmpt == 4 : 
        return  False
    else :
        return True

def coup_possible(plateau,coup,coord,touffe):
    """
    Fonction que return True si le coup déplace des moutons sinon return False.
    Paramètres : 
     plateau,coord,touffe = listes
     coup = int
    Return : Booléen 
    plateau = [['S', 'G', 'B', 'B', None], [None, 'B', 'SG', None, None]]
    coup = 0
    coord = [(0,0),(1,2)]
    touffe = [(0,1),(1,2)]
    >>> coup_possibe(plateau,coup,coord,touffe)
    True
    """
    lst = ["right","left","up","down"]
    plateau2,coord2 = deplacement(plateau,lst[coup],coord,touffe)
    if comparaison(coord,coord2) : 
        return True
    else : 
        return False
   
def comparaison(lst1, lst2):
    """
    Fonction qui compare deux listes, si elles sont identiques, renvoie False.
    
    Paramètres : listes 
    Return : Booléen


    lst = [0,1,2]
    lst1 = [0,1,2]
    lst2 = [0,1,2,3]
    >>> comparaison(lst,lst1)
    False
    >>> comparaison(lst1,lst2)
    True

    """
    
    if lst1 == lst2: 
        return False
    else : 
        return True
    