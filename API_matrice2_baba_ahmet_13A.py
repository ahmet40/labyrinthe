def construit_matrice(nb_lignes,nb_colonnes,valeur_par_defaut =None):
    """
    construit une liste de liste pour representer la matrice
    
    """
    matrice=[]
    for nbre_ligne in range(nb_lignes):
        liste_a_ajouter=[]
        for nbre_colonne in range(nb_colonnes):
            liste_a_ajouter.append(valeur_par_defaut)
        matrice.append(liste_a_ajouter)
    return matrice




def get_nb_lignes(matrice):
    """
    Fonction qui permet de determiner combien de ligne contient la matrice
    parametre:
        entrer:
            une matrice (tuple) : ligne,colonne,matrice
        sortie:
            entier 
    """
    return len(matrice)

def get_nb_colonnes(matrice):
    """
    Fonction qui permet de determiner le nombre de colonne que la matrice contient
    parametre:
        entrer:
            une matrice (tuple) : ligne,colonne,matrice
        sortie:
            entier 
    """
    return len(matrice[0])

def get_val(matrice,ligne,colonne):
    """
    Fonction qui permet de determiner la valeur de la matrice au coordonnee ligne,colonne
    parametre:
        entrer:
            une matrice (tuple) : ligne,colonne,matrice
        sortie:
            entier 
    """
    if ligne <  get_nb_lignes(matrice) and colonne < get_nb_colonnes(matrice):
        return matrice[ligne][colonne]

def set_val (matrice,ligne,colonne,nouvelle_valeur):
    """
    Fonction qui permet de changer la valeur de la matrice au coordonnee ligne,colonne
    parametre:
        entrer:
            une matrice (tuple) : ligne,colonne,matrice
        sortie:
            entier 
    """
    if ligne <  get_nb_lignes(matrice) and colonne < get_nb_colonnes(matrice):
        matrice[ligne][colonne] = nouvelle_valeur


def get_ligne(matrice,ligne):
    """
    Fonction qui renvoie les valeur de la matrice qui se trouvent à la ligne donne
    parametre:
        entrer:
            une matrice (tuple) : ligne,colonne,matrice
        sortie:
            liste 
    """
    if ligne <  get_nb_lignes(matrice):
        return matrice[ligne]


def get_colonne(matrice,colonne):
    """
    Fonction qui renvoie les valeur de la matrice qui se trouvent à la ligne donne
    parametre:
        entrer:
            une matrice (tuple) : ligne,colonne,matrice
        sortie:
            liste
    """
    if colonne < get_nb_colonnes(matrice):
        return [ligne[colonne] for ligne in matrice]


def get_diagonale_principale(matrice):
    """
    Fonction qui renvoie la diagonale principale matrice
    parametre:
        entrer:
            une matrice (tuple) : ligne,colonne,matrice
        sortie:
            liste
    """
    if get_nb_colonnes(matrice) == get_nb_lignes(matrice):
        return [matrice[ligne][ligne] for ligne in range(len(matrice))]


def get_diagonale_secondaire(matrice):
    """
    Fonction qui renvoie la diagonale secondaire matrice
    parametre:
        entrer:
            une matrice (tuple) : ligne,colonne,matrice
        sortie:
            liste
    """
    if get_nb_colonnes(matrice) == get_nb_lignes(matrice):
        return [matrice[ligne][len(matrice)-1-ligne] for ligne in range(len(matrice))]


def transpose(matrice):
    """
    Fonction qui renvoie la transpose de la matrice
    parametre:
        entrer:
            une matrice (tuple) : ligne,colonne,matrice
        sortie:
            liste de liste
    """
    if get_nb_colonnes(matrice) == get_nb_lignes(matrice):
        return [get_colonne(matrice,colonne) for colonne in range(get_nb_colonnes(matrice))]    

def is_triangulaire_inf(matrice):
    """
	Cette fonction vous dit si la matrice donné est traingulaire inferieur ou non
	Args:
		entrer:
			Matrice une liste de liste.
		sortie:
			bool
    """
    if get_nb_colonnes(matrice) == get_nb_lignes(matrice):
        for ligne in range(len(matrice)):
            liste=matrice[ligne][ligne+1:]      #prend les valeurs de la matrice dont nous avons besoin pour savoir si il est triangulaire inferieur
            for valeur in liste:
                if valeur != 0:
                    return False
        return True
