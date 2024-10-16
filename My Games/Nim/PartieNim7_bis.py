import fltk
from fct_graphique_bis import *
from random import *
nb_baton = 21
x = 800
y = 800

def fin_de_manche(lst):
    for i in range(len(lst)):
        if len(lst[i]) != 0:
            return 1
    return 0

def binaire(batons):
    bin = [0,1,10,11,100,101,110,111]
    return bin[batons]
    
def verif(cdc):
    for chose in range(len(cdc)):
        if int(cdc[chose]) % 2 != 0:
            return False
    return True

def fltk_marinbad_bot(d,f,c):
    nb_objets=[[1,2,3,4,5,6,7],[1,2,3,4,5],[1,2,3],[1]]
    n=0
    if d == 1:
        n=jeu(n+1)
    while fin_de_manche(nb_objets):
        n=jeu(n+1)
        for w in range(len(nb_objets)):
            for z in range(len(nb_objets[w])):
                fltk.rectangle(x/80+(x/30)*z,y/2+(50*(-3+w)+20*(-3+w)), (x+x)/80+(x/30)*z, (y/2)+50+(50*(-3+w)+20*(-3+w)), remplissage="beige")
                fltk.cercle(15+(x/30)*z, (y/2)+5+(50*(-3+w)+20*(-3+w)), x/100, remplissage="red")
        baton_choisi = []
        while True:
            if n == 0:  
                fltk.texte(x/2 , 50, 'Au tour du joueur ' + str(n+1), ancrage='center')
                fltk.texte(x/2, 100, 'Cliquez sur les allumettes que vous voulez prendre.', ancrage='center')
                ev = fltk.donne_ev()
                tev = fltk.type_ev(ev)
                if len(baton_choisi)>0:
                    fltk.rectangle(x-200,y-200,x-100,y-100,tag = 'rect')
                    fltk.texte(x-150 , y-150, 'Fini', ancrage='center', tag = 'fin')
                else:
                    fltk.efface('rect')
                    fltk.efface('fin')
                if tev == 'ClicGauche':
                    if len(baton_choisi)>0:
                        if x-200 < fltk.abscisse(ev) < x-100 or y-200 < fltk.ordonnee(ev) < y-100 :
                            break
                    for i in range(len(nb_objets)):
                        for j in range(len(nb_objets[i])):
                            if (x+x)/80+(x/30)*j+5 > fltk.abscisse(ev) > x/80+(x/30)*j-5 and (y/2)+50+(50*(-3+i)+20*(-3+i)) > fltk.ordonnee(ev) > y/2+(50*(-3+i)+20*(-3+i)) :
                                if (i,j) in baton_choisi:
                                    fltk.efface_tout()
                                    baton_choisi.remove((i,j))
                                    for w in range(len(nb_objets)):
                                        for z in range(len(nb_objets[w])):
                                            fltk.rectangle(x/80+(x/30)*z,y/2+(50*(-3+w)+20*(-3+w)), (x+x)/80+(x/30)*z, (y/2)+50+(50*(-3+w)+20*(-3+w)), remplissage="beige")
                                            fltk.cercle(15+(x/30)*z, (y/2)+5+(50*(-3+w)+20*(-3+w)), x/100, remplissage="red")
                                    for l in range(len(baton_choisi)):
                                        fltk.rectangle(x/130+(x/30)*baton_choisi[l][1],y/2-10+(50*(-3+baton_choisi[l][0])+20*(-3+baton_choisi[l][0])), (x+x)/65+(x/30)*baton_choisi[l][1], (y/2)+60+(50*(-3+baton_choisi[l][0])+20*(-3+baton_choisi[l][0])), couleur='yellow')
                                else:
                                    if len(baton_choisi) > 0:
                                        if i != baton_choisi[0][0]:
                                            fltk.texte(100 , 50, 'Impossible !', ancrage='center', tag = 'pbl')
                                            fltk.attente(1)
                                            fltk.efface('pbl')
                                        else:
                                            fltk.rectangle(x/130+(x/30)*j,y/2-10+(50*(-3+i)+20*(-3+i)), (x+x)/65+(x/30)*j, (y/2)+60+(50*(-3+i)+20*(-3+i)), couleur='yellow')
                                            baton_choisi.append((i,j))
                                    else:
                                        fltk.rectangle(x/130+(x/30)*j,y/2-10+(50*(-3+i)+20*(-3+i)), (x+x)/65+(x/30)*j, (y/2)+60+(50*(-3+i)+20*(-3+i)), couleur='yellow')
                                        baton_choisi.append((i,j))
                else:
                    pass
            else:  
                if c == 1:   
                    col = randint(1,4)
                    while len(nb_objets[col-1]) == 0:
                        col = randint(1,4)
                    nb_tonba = randint(1,len(nb_objets[col-1]))
                    break
                else:
                    if f == 2:
                        test0 = 0
                        test1 = 0
                        test2 = 0

                        for rah in range(len(nb_objets)):
                            if len(nb_objets[rah]) == 1:
                                test1 += 1
                            elif len(nb_objets[rah]) >= 2:
                                test2 += 1
                            elif len(nb_objets[rah]) == 0:
                                test0 += 1
                        print(test1,test2,test0)
                        if (test0 == 2 or test0 == 0) and (test1 == 1 or test1 == 3) and test2 == 1:
                            print('ah')
                            for something in range(len(nb_objets)):
                                if len(nb_objets[something]) >= 2:
                                    col = something + 1
                            nb_tonba = len(nb_objets[col-1])
                            break
                        elif test0 == 1 and test1 == 2 and test2 == 1:
                            for something in range(len(nb_objets)):
                                if len(nb_objets[something]) >= 2:
                                    col = something + 1
                            nb_tonba = len(nb_objets[col-1])-1
                            break
                    total_binaire = 0
                    for truc in range(len(nb_objets)):
                        total_binaire += binaire(len(nb_objets[truc]))
                    if verif(str(total_binaire)):
                        col = randint(1,4)
                        while len(nb_objets[col-1]) == 0:
                            col = randint(1,4)
                        nb_tonba = randint(1,len(nb_objets[col-1]))
                        break
                    else:
                        col = randint(1,4)
                        while len(nb_objets[col-1]) == 0:
                            col = randint(1,4)
                        nb_tonba = randint(1,len(nb_objets[col-1]))
                        while not verif(str(total_binaire-binaire(len(nb_objets[col-1]))+binaire(len(nb_objets[col-1])-nb_tonba))):
                            col = randint(1,4)
                            while len(nb_objets[col-1]) == 0:
                                col = randint(1,4)
                            nb_tonba = randint(1,len(nb_objets[col-1]))
                        break
            fltk.mise_a_jour()
        fltk.efface_tout()
        if n == 0:
            for h in range (len(baton_choisi)):
                nb_objets[baton_choisi[0][0]].pop()
        else:
            for life_is_hard in range(nb_tonba):
                nb_objets[col-1].pop()
    if f == 2 :
        n = jeu(n+1)
    fltk.texte(x/2,y/2,'Le joueur '+str(n+1)+' a gagné !' , ancrage='center')
    fltk.attente(5)
    fltk.ferme_fenetre()

def fltk_marinbad(d,f):
    
    nb_objets=[[1,2,3,4,5,6,7],[1,2,3,4,5],[1,2,3],[1]]
    n=0
    if d == 1:
        n=jeu(n+1)
    while fin_de_manche(nb_objets):
        n=jeu(n+1)
        for w in range(len(nb_objets)):
            for z in range(len(nb_objets[w])):
                fltk.rectangle(x/80+(x/30)*z,y/2+(50*(-3+w)+20*(-3+w)), (x+x)/80+(x/30)*z, (y/2)+50+(50*(-3+w)+20*(-3+w)), remplissage="beige")
                fltk.cercle(15+(x/30)*z, (y/2)+5+(50*(-3+w)+20*(-3+w)), x/100, remplissage="red")
        baton_choisi = []
        while True:  
            fltk.texte(x/2 , 50, 'Au tour du joueur ' + str(n+1), ancrage='center')
            fltk.texte(x/2, 100, 'Cliquez sur les allumettes que vous voulez prendre.', ancrage='center')
            ev = fltk.donne_ev()
            tev = fltk.type_ev(ev)
            if len(baton_choisi)>0:
                fltk.rectangle(x-200,y-200,x-100,y-100,tag = 'rect')
                fltk.texte(x-150 , y-150, 'Fini', ancrage='center', tag = 'fin')
            else:
                fltk.efface('rect')
                fltk.efface('fin')
            if tev == 'ClicGauche':
                if len(baton_choisi)>0:
                    if x-200 < fltk.abscisse(ev) < x-100 or y-200 < fltk.ordonnee(ev) < y-100 :
                        break
                for i in range(len(nb_objets)):
                    for j in range(len(nb_objets[i])):
                        if (x+x)/80+(x/30)*j+5 > fltk.abscisse(ev) > x/80+(x/30)*j-5 and (y/2)+50+(50*(-3+i)+20*(-3+i)) > fltk.ordonnee(ev) > y/2+(50*(-3+i)+20*(-3+i)) :
                            if (i,j) in baton_choisi:
                                fltk.efface_tout()
                                baton_choisi.remove((i,j))
                                for w in range(len(nb_objets)):
                                    for z in range(len(nb_objets[w])):
                                        fltk.rectangle(x/80+(x/30)*z,y/2+(50*(-3+w)+20*(-3+w)), (x+x)/80+(x/30)*z, (y/2)+50+(50*(-3+w)+20*(-3+w)), remplissage="beige")
                                        fltk.cercle(15+(x/30)*z, (y/2)+5+(50*(-3+w)+20*(-3+w)), x/100, remplissage="red")
                                for l in range(len(baton_choisi)):
                                    fltk.rectangle(x/130+(x/30)*baton_choisi[l][1],y/2-10+(50*(-3+baton_choisi[l][0])+20*(-3+baton_choisi[l][0])), (x+x)/65+(x/30)*baton_choisi[l][1], (y/2)+60+(50*(-3+baton_choisi[l][0])+20*(-3+baton_choisi[l][0])), couleur='yellow')
                            else:
                                if len(baton_choisi) > 0:
                                    if i != baton_choisi[0][0]:
                                        fltk.texte(100 , 50, 'Impossible !', ancrage='center', tag = 'pbl')
                                        fltk.attente(1)
                                        fltk.efface('pbl')
                                    else:
                                        fltk.rectangle(x/130+(x/30)*j,y/2-10+(50*(-3+i)+20*(-3+i)), (x+x)/65+(x/30)*j, (y/2)+60+(50*(-3+i)+20*(-3+i)), couleur='yellow')
                                        baton_choisi.append((i,j))
                                else:
                                    fltk.rectangle(x/130+(x/30)*j,y/2-10+(50*(-3+i)+20*(-3+i)), (x+x)/65+(x/30)*j, (y/2)+60+(50*(-3+i)+20*(-3+i)), couleur='yellow')
                                    baton_choisi.append((i,j))
            else:
                pass
            fltk.mise_a_jour()
        fltk.efface_tout()
        for h in range (len(baton_choisi)):
            nb_objets[baton_choisi[0][0]].pop()
    if f == 2 :
        n = jeu(n+1)
    fltk.texte(x/2,y/2,'Le joueur '+str(n+1)+' a gagné !' , ancrage='center')
    fltk.attente(5)
    fltk.ferme_fenetre()
            

def fltk_nim(d,f):
    nb_objet=21
    n=0
    if d == 1:
        n=jeu(n+1)
    while nb_objet>0:
        n=jeu(n+1)
        for i in range(nb_objet):
            fltk.rectangle(x/80+(x/30)*i,(y/2)-50, (x+x)/80+(x/30)*i, (y/2)+50, remplissage="beige")
            fltk.cercle(15+(x/30)*i, (y/2)-55, x/100, remplissage="red")
        baton_choisi = []
        while True:  
            fltk.texte(x/2 , 50, 'Au tour du joueur ' + str(n+1), ancrage='center')
            fltk.texte(x/2, 100, 'Cliquez sur les allumettes que vous voulez prendre.', ancrage='center')
            ev = fltk.donne_ev()
            tev = fltk.type_ev(ev)
            if len(baton_choisi)>0:
                fltk.rectangle(x-200,y-200,x-100,y-100,tag = 'rect')
                fltk.texte(x-150 , y-150, 'Fini', ancrage='center', tag = 'fin')
            else:
                fltk.efface('rect')
                fltk.efface('fin')
            if tev == 'ClicGauche':
                if len(baton_choisi)>0:
                    if x-200 < fltk.abscisse(ev) < x-100 or y-200 < fltk.ordonnee(ev) < y-100 :
                        break
                for i in range(1):
                    for j in range(nb_objet):
                        if (x+x)/80+(x/30)*j+5 > fltk.abscisse(ev) > x/80+(x/30)*j-5 and (y/2)+60 > fltk.ordonnee(ev) > (y/2.5)+10 :
                            if j in baton_choisi:
                                fltk.efface_tout()
                                baton_choisi.remove(j)
                                for k in range(nb_objet):
                                    fltk.rectangle(x/80+(x/30)*k,(y/2)-50, (x+x)/80+(x/30)*k, (y/2)+50, remplissage="beige")
                                    fltk.cercle(15+(x/30)*k, (y/2)-55, x/100, remplissage="red")
                                for l in range(len(baton_choisi)):
                                    fltk.rectangle(x/80+(x/30)*baton_choisi[l]-5, (y/2.5)+x/100, (x+x)/80+(x/30)*baton_choisi[l]+5, (y/2)+60, couleur='yellow')
                            else:
                                if len(baton_choisi) == 3:
                                    fltk.texte(100 , 50, 'Impossible !', ancrage='center', tag = 'pbl')
                                    fltk.attente(1)
                                    fltk.efface('pbl')
                                else:
                                    fltk.rectangle(x/80+(x/30)*j-5, (y/2.5)+10, (x+x)/80+(x/30)*j+5, (y/2)+60, couleur='yellow')
                                    baton_choisi.append(j)
            else:
                pass
            fltk.mise_a_jour()
        fltk.efface_tout()
        nb_objet -= len(baton_choisi)
    if f == 2 :
        n = jeu(n+1)
    fltk.texte(x/2,y/2,'Le joueur '+str(n+1)+' a gagné !' , ancrage='center')
    fltk.attente(5)
    fltk.ferme_fenetre()
    
def fltk_nim_bot(d,f,c):
    nb_objet=21
    n=0
    bot1 = 0
    if d == 1:
        n=jeu(n+1)
    while nb_objet>0:
        n=jeu(n+1)
        for i in range(nb_objet):
            fltk.rectangle(x/80+(x/30)*i,(y/2)-50, (x+x)/80+(x/30)*i, (y/2)+50, remplissage="beige")
            fltk.cercle(15+(x/30)*i, (y/2)-55, x/100, remplissage="red")
        baton_choisi = []
        while True:  
            if n == 0:
                fltk.texte(x/2 , 50, 'A vous joueur', ancrage='center')
                fltk.texte(x/2, 100, 'Cliquez sur les allumettes que vous voulez prendre.', ancrage='center')
                if bot1 != 0:
                    fltk.texte(700 , y/2, f'{(bot1)} batons.', ancrage='center')
                ev = fltk.donne_ev()
                tev = fltk.type_ev(ev)
                if len(baton_choisi)>0:
                    fltk.rectangle(x-200,y-200,x-100,y-100,tag = 'rect')
                    fltk.texte(x-150 , y-150, 'Fini', ancrage='center', tag = 'fin')
                else:
                    fltk.efface('rect')
                    fltk.efface('fin')
                if tev == 'ClicGauche':
                    if len(baton_choisi)>0:
                        if x-200 < fltk.abscisse(ev) < x-100 or y-200 < fltk.ordonnee(ev) < y-100 :
                            break
                    for i in range(1):
                        for j in range(nb_objet):
                            if (x+x)/80+(x/30)*j+5 > fltk.abscisse(ev) > x/80+(x/30)*j-5 and (y/2)+60 > fltk.ordonnee(ev) > (y/2.5)+10 :
                                if j in baton_choisi:
                                    fltk.efface_tout()
                                    baton_choisi.remove(j)
                                    for k in range(nb_objet):
                                        fltk.rectangle(x/80+(x/30)*k,(y/2)-50, (x+x)/80+(x/30)*k, (y/2)+50, remplissage="beige")
                                        fltk.cercle(15+(x/30)*k, (y/2)-55, x/100, remplissage="red")
                                    for l in range(len(baton_choisi)):
                                        fltk.rectangle(x/80+(x/30)*baton_choisi[l]-5, (y/2.5)+10, (x+x)/80+(x/30)*baton_choisi[l]+5, (y/2)+60, couleur='yellow')
                                else:
                                    if len(baton_choisi) == 3:
                                        fltk.texte(100 , 50, 'Impossible !', ancrage='center', tag = 'pbl')
                                        fltk.attente(1)
                                        fltk.efface('pbl')
                                    else:
                                        fltk.rectangle(x/80+(x/30)*j-5, (y/2.5)+10, (x+x)/80+(x/30)*j+5, (y/2)+60, couleur='yellow')
                                        baton_choisi.append(j)
                else:
                    pass
            else:
                
                if f == 1:
                    if c == 1:
                        bot1 = randint(1,3)
                        while bot1 > nb_objet:
                            bot1 = randint(1,3)
                    else:
                        if nb_objet == 21:
                            bot1 = 1
                        else:
                            if nb_objet%4==0:
                                bot1 = randint (1,3)
                                while bot1 > nb_objet:
                                    bot1 = randint(1,3)
                            else:
                                bot1 = randint(1,3)
                                while (nb_objet - bot1) % 4 != 0:
                                    bot1 = randint(1,3)
                    break
                else:
                    if c == 1:
                        bot1 = randint(1,3)
                        while bot1 > nb_objet:
                            bot1 = randint(1,3)
                    else:
                        if nb_objet == 21:
                            bot1=randint(1,3)
                        else:
                            if d == 1:
                                bot1 = 4 - len(baton_choisi)
                            else:
                                if (21 - nb_objet)%4==0:
                                    bot1 = randint (1,3)
                                    while bot1 > nb_objet:
                                        bot1 = randint(1,3)
                                    
                                else:
                                    bot1 = randint(1,3)
                                    while (21-nb_objet+bot1)%4!=0:
                                        bot1 = randint(1,3)
                    break
            fltk.mise_a_jour()
        fltk.efface_tout()
        if n == 0:
            nb_objet -= len(baton_choisi)
        else:
            nb_objet -= bot1
    if f == 2 :
        n = jeu(n+1)
    fltk.texte(x/2,y/2,'Le joueur '+str(n+1)+' a gagné !' , ancrage='center')
    fltk.attente(5)
    fltk.ferme_fenetre()


def jeu(n):
    n= n%2
    return n

fltk.cree_fenetre(x,y)
a,b,c,d,e,f = init()
if a == 2:
    fltk.ferme_fenetre()
elif b==2:
    if e == 1:
        fltk_nim_bot(d,f,c)
    else:
        fltk_marinbad_bot(d,f,c)
else: 
    if e == 2:
        fltk_marinbad(d,f)
    else:
        fltk_nim(d,f)
