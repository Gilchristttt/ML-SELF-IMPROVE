
def victoire(plateau): 
    """
    Fonction qui détermine la victoire, si une case dans le plateau est une touffe d'herbe return False.
    Sinon return True 
    """
    for col in plateau : 
        for case in col : 
            if case == "G" : 
                return False 
    return True

def recherche(plateau,dire,coord):
    position = deplacement(plateau,dire,coord)
    if victoire(position):
        return True
    else:
        return False
def solveur(plateau,etat,direction):
    """
    etat = les coordonnées des moutons
    direction =    ['Left', 'Right', 'Up', 'Down']

    """

    visite = set()
    if victoire(plateau):
        return []
    if etat in visite:
        return None
    else:
        visite.add(tuple(etat))
        dire = direction[0]
        etat = deplacement(plateau,dire,coord)
        solveur(plateau,etat,direction)
        if recherche(plateau,dire,coord):
            return [dire + coord]
        else:
            dire = direction[1:]
            etat = deplacement(plateau,dire,coord)
            solveur(plateau,etat,direction)
