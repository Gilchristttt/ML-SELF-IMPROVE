from random import*


def bot_simple(liste, lst_col):
    col = choice(lst_col)
    lst_col = liste[col-1]
    if len(liste) == 1:
        if len(lst_col) < 3:
            lin = choice(lst_col)
            return lin, col
        lin = randint(1, 3)
        return lin, col
    lin = choice(lst_col)
    return lin, col

def bot_dur_nim_normal(liste, lst_col):
    col = choice(lst_col)
    lst_col = liste[col-1]
    if len(lst_col) % 4 == 1:
        return 1, col
    if len(lst_col) % 4 == 2:
        return 2, col
    if len(lst_col) % 4 == 3:
        return 3, col
    if len(lst_col) < 3:
        lin = choice(lst_col)
        return lin, col
    lin = randint(1, 3)
    return lin, col

def bot_dur_nim_misere(liste, lst_col):
    col = choice(lst_col)
    lst_col = liste[col-1]
    if len(lst_col) % 4 == 1:
        if len(lst_col) < 3:
            lin = choice(lst_col)
            return lin, col
        lin = randint(1, 3)
        return lin, col
    if len(lst_col) % 4 == 2:
        return 1, col
    if len(lst_col) % 4 == 3:
        return 2, col
    if len(lst_col) % 4 == 0:
        return 3, col

def choix_bot(difficulte, jeu, mode, liste, lst_col):
    if difficulte == 1:
        return bot_simple(liste, lst_col)
    if difficulte == 2 and jeu == 1 and mode == 1:
        return bot_dur_nim_normal(liste, lst_col)
    if difficulte == 2 and jeu == 1 and mode == 2:
        return bot_dur_nim_misere(liste, lst_col)