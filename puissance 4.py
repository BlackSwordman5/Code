Tableau = [ [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0]     ] # 0 = case vide, 1 = 'X' , -1 = 'O'

def placement_pion(Tableau,numéro_joueur):
    #numéro_joueur = 1 si X ou -1 si O
    colonne_remplie = True
    while colonne_remplie == True:
        num_colonne = int(input("Donne un numéro de colonne"))
        num_ligne = 5
        while Tableau[num_ligne][num_colonne] !=0 and num_ligne > -1:
            num_ligne -= 1
        if num_ligne != -1:
            Tableau[num_ligne][num_colonne] = numéro_joueur
            colonne_remplie = False
        else:
            print("colonne déjà remplie")
    return Tableau

def affichage(Tableau):
    for ligne in range(0,6):
        for colonne in range(0,8):
            if Tableau[ligne][colonne] == 1:
                print('| X |',end='')
            elif Tableau[ligne][colonne] == -1:
                print('| O |',end='')
            else:
                print('|   |',end='')
        print('')

def test_si_alignement_horizontal(Tableau):
    gagnant = 0
    for ligne in range(0,6):
        for colonne in range(0,5):
            L = Tableau[ligne][colonne]+Tableau[ligne][colonne+1]+Tableau[ligne][colonne+2]+Tableau[ligne][colonne+3]
            if L == 4:
                print('les X gagnent')
                gagnant = 1
            elif L ==-4:
                print('les O gagnent')
                gagnant = -1
    return gagnant

def test_si_alignement_vertical(Tableau):
    gagnant = 0
    for ligne in range(0,3):
        for colonne in range(0,8):
            L = Tableau[ligne][colonne]+Tableau[ligne+1][colonne]+Tableau[ligne+2][colonne]+Tableau[ligne+3][colonne]
            if L == 4:
                print('les X gagnent')
                gagnant = 1
            elif L ==-4:
                print('les O gagnent')
                gagnant = -1
    return gagnant

def test_si_alignement_diagonal(Tableau):
    gagnant = 0
    for ligne in range(3,6):
        for colonne in range(0,5):
            L = Tableau[ligne][colonne]+Tableau[ligne+1][colonne+1]+Tableau[ligne+2][colonne+2]+Tableau[ligne+3][colonne+3]
            if L == 4:
                print('les X gagnent')
                gagnant = 1
            elif L ==-4:
                print('les O gagnent')
                gagnant = -1
    return gagnant

def test_si_alignement_diagonal2(Tableau):
    gagnant = 0
    for ligne in range(3,6):
        for colonne in range(0,5):
            L = Tableau[ligne][colonne]+Tableau[ligne-1][colonne+1]+Tableau[ligne-2][colonne+2]+Tableau[ligne-3][colonne+3]
            if L == 4:
                print('les X gagnent')
                gagnant = 1
            elif L ==-4:
                print('les O gagnent')
                gagnant = -1
    return gagnant


# corps principal du programme

numéro_joueur = 1
compteur_de_pion = 0
poursuite_programme = True
affichage(Tableau)

while poursuite_programme:
    placement_pion(Tableau,numéro_joueur)
    compteur_de_pion =+ 1
    affichage(Tableau)
    qui_gagne = test_si_alignement_horizontal(Tableau)
    qui_gagne_2 = test_si_alignement_vertical(Tableau)
    qui_gagne_3 = test_si_alignement_diagonal(Tableau)
    qui_gagne_4 = test_si_alignement_diagonal2(Tableau)
    if qui_gagne != 0 or qui_gagne_2 != 0 or compteur_de_pion == 48:
        poursuite_prgramme = False
    numéro_joueur =- numéro_joueur


