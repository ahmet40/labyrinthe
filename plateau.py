"""
Permet de modéliser un le_plateau de jeu avec :
    - une matrice qui contient des nombres entiers
    - chaque nombre entier correspond à un item :
      MUR, COULOIR, PERSONNAGE, FANTOME
"""
import matrice

MUR = 1
COULOIR = 0
PERSONNAGE = 2
FANTOME = 3

NORD = 'z'
OUEST = 'q'
SUD = 's'
EST = 'd'


def init(nom_fichier="./labyrinthe1.txt"):
    """Construit le plateau de jeu de la façon suivante :
        - crée une matrice à partir d'un fichier texte qui contient des COULOIR et MUR
        - met le PERSONNAGE en haut à gauche cad à la position (0, 0)
        - place un FANTOME en bas à droite
    Args:
        nom_fichier (str, optional): chemin vers un fichier csv qui contient COULOIR et MUR.
        Defaults to "./labyrinthe1.txt".

    Returns:
        le plateau de jeu avec les MUR, COULOIR, PERSONNAGE et FANTOME
    """
    ma_matrice=matrice.charge_matrice(nom_fichier,type_valeur='int')
    matrice.set_val(ma_matrice,0,0,2)
    matrice.set_val(ma_matrice,matrice.get_nb_lignes(ma_matrice)-1,matrice.get_nb_colonnes(ma_matrice)-1,3)
    return ma_matrice


def est_sur_le_plateau(le_plateau, position):
    """Indique si la position est bien sur le plateau

    Args:
        le_plateau (plateau): un plateau de jeu
        position (tuple): un tuple de deux entiers de la forme (no_ligne, no_colonne) 

    Returns:
        [boolean]: True si la position est bien sur le plateau
    """
    return position[0] in range(matrice.get_nb_lignes(le_plateau)) and position[1] in range(matrice.get_nb_colonnes(le_plateau))


def get(le_plateau, position):
    """renvoie la valeur de la case qui se trouve à la position donnée

    Args:
        le_plateau (plateau): un plateau de jeu
        position (tuple): un tuple d'entiers de la forme (no_ligne, no_colonne)

    Returns:
        int: la valeur de la case qui se trouve à la position donnée ou
             None si la position n'est pas sur le plateau
    """
    if est_sur_le_plateau(le_plateau,position):
        return matrice.get_val(le_plateau,position[0],position[1])


def est_un_mur(le_plateau, position):
    """détermine s'il y a un mur à la poistion donnée

    Args:
        le_plateau (plateau): un plateau de jeu
        position (tuple): un tuple d'entiers de la forme (no_ligne, no_colonne)

    Returns:
        bool: True si la case à la position donnée est un MUR, False sinon
    """
    if est_sur_le_plateau(le_plateau,position):
        return matrice.get_val(le_plateau,position[0],position[1]) ==1


def contient_fantome(le_plateau, position):
    """Détermine s'il y a un fantôme à la position donnée

    Args:
        le_plateau (plateau): un plateau de jeu
        position (tuple): un tuple de deux entiers de la forme (no_ligne, no_colonne) 

    Returns:
        bool: True si la case à la position donnée est un FANTOME, False sinon
    """
    if est_sur_le_plateau(le_plateau,position):
        return matrice.get_val(le_plateau,position[0],position[1]) ==3

def est_la_sortie(le_plateau, position):
    """Détermine si la position donnée est la sortie
       cad la case en bas à droite du labyrinthe

    Args:
        le_plateau (plateau): un plateau de jeu
        position (tuple): un tuple de deux entiers de la forme (no_ligne, no_colonne) 

    Returns:
        bool: True si la case à la position donnée est la sortie, False sinon
    """
    if est_sur_le_plateau(le_plateau,position):
        return position[0] == matrice.get_nb_lignes(le_plateau)-1 and position[1] == matrice.get_nb_colonnes(le_plateau)-1


def deplace_personnage(le_plateau, personnage, direction):
    """déplace le PERSONNAGE sur le plateau si le déplacement est valide
       Le personnage ne peut pas sortir du plateau ni traverser les murs
       Si le déplacement n'est pas valide, le personnage reste sur place

    Args:
        le_plateau (plateau): un plateau de jeu
        personnage (tuple): la position du personnage sur le plateau
        direction (str): la direction de déplacement SUD, EST, NORD, OUEST

    Returns:
        [tuple]: la nouvelle position du personnage
    """
    if direction == EST:
        nv_position=personnage[0],personnage[1]+1

        if est_sur_le_plateau(le_plateau,nv_position) and not est_un_mur(le_plateau,nv_position) and not contient_fantome(le_plateau,nv_position):
            matrice.set_val(le_plateau,nv_position[0],nv_position[1],2)
            matrice.set_val(le_plateau,personnage[0],personnage[1],0)
            return nv_position

        else:
            return personnage
    elif direction == NORD:
        nv_position=personnage[0]-1,personnage[1]

        if est_sur_le_plateau(le_plateau,nv_position) and not est_un_mur(le_plateau,nv_position) and not contient_fantome(le_plateau,nv_position):
            matrice.set_val(le_plateau,nv_position[0],nv_position[1],2)
            matrice.set_val(le_plateau,personnage[0],personnage[1],0)
            return nv_position

        else:
            return personnage
    elif direction == SUD:
        nv_position=personnage[0]+1,personnage[1]

        if est_sur_le_plateau(le_plateau,nv_position) and not est_un_mur(le_plateau,nv_position) and not contient_fantome(le_plateau,nv_position):
            matrice.set_val(le_plateau,nv_position[0],nv_position[1],2)
            matrice.set_val(le_plateau,personnage[0],personnage[1],0)
            return nv_position

        else:
            return personnage
    if direction == OUEST:
        nv_position=personnage[0],personnage[1]-1

        if est_sur_le_plateau(le_plateau,nv_position) and not est_un_mur(le_plateau,nv_position) and not contient_fantome(le_plateau,nv_position):
            matrice.set_val(le_plateau,nv_position[0],nv_position[1],2)
            matrice.set_val(le_plateau,personnage[0],personnage[1],0)
            return nv_position

        else:
            return personnage
    if direction == None:
        if est_sur_le_plateau(le_plateau,personnage) and  get(le_plateau,personnage) == 0:
            return COULOIR
        else:
            return PERSONNAGE



def voisins(le_plateau, position):
    """Renvoie l'ensemble des positions cases voisines accessibles de la position renseignées
       Une case accessible est une case qui est sur le plateau et qui n'est pas un mur
    Args:
        le_plateau (plateau): un plateau de jeu
        position (tuple): un tuple de deux entiers de la forme (no_ligne, no_colonne) 

    Returns:
        set: l'ensemble des positions des cases voisines accessibles
    """
    if est_sur_le_plateau(le_plateau,position):
        ensemble_position=set()
        nv_position=position[0],position[1]+1
        if est_sur_le_plateau(le_plateau,nv_position) and not est_un_mur(le_plateau,nv_position):
            ensemble_position.add(nv_position)

        nv_position=position[0],position[1]-1
        if est_sur_le_plateau(le_plateau,nv_position) and not est_un_mur(le_plateau,nv_position):
            ensemble_position.add(nv_position)

        nv_position=position[0]+1,position[1]
        if est_sur_le_plateau(le_plateau,nv_position) and not est_un_mur(le_plateau,nv_position):
            ensemble_position.add(nv_position)

        nv_position=position[0]-1,position[1]
        if est_sur_le_plateau(le_plateau,nv_position) and not est_un_mur(le_plateau,nv_position):
            ensemble_position.add(nv_position)
        return ensemble_position



def fabrique_le_calque(le_plateau, position_depart):
    """fabrique le calque d'un labyrinthe en utilisation le principe de l'inondation :
       
    Args:
        le_plateau (plateau): un plateau de jeu
        position_depart (tuple): un tuple de deux entiers de la forme (no_ligne, no_colonne) 

    Returns:
        matrice: une matrice qui a la taille du plateau dont la case qui se trouve à la
       position_de_depart est à 0 les autres cases contiennent la longueur du
       plus court chemin pour y arriver (les murs et les cases innaccessibles sont à None)
    """
    ma_matrice=matrice.new_matrice(matrice.get_nb_lignes(le_plateau),matrice.get_nb_colonnes(le_plateau),None)
    matrice.set_val(ma_matrice,position_depart[0],position_depart[1],0)
    ensemble_voisins=voisins(le_plateau,(position_depart[0],position_depart[1]))
    valeur=0
    while ensemble_voisins != set():
        ens=set()
        valeur+=1
        for voisin in ensemble_voisins:
            matrice.set_val(ma_matrice,voisin[0],voisin[1],valeur) 
            ses_voisin=voisins(le_plateau,(voisin[0],voisin[1]))
            for voisin2 in ses_voisin:
                if get(ma_matrice,(voisin2[0],voisin2[1])) == None:
                    ens.add(voisin2)
        ensemble_voisins = ens
    return ma_matrice
        

le_plateau = init()
matrice.affiche(fabrique_le_calque(le_plateau,(4,5)))

def fabrique_chemin(le_plateau, position_depart, position_arrivee):

    """Renvoie le plus court chemin entre position_depart position_arrivee

    Args:
        le_plateau (plateau): un plateau de jeu
        position_depart (tuple): un tuple de deux entiers de la forme (no_ligne, no_colonne) 
        position_arrivee (tuple): un tuple de deux entiers de la forme (no_ligne, no_colonne) 

    Returns:
        list: Une liste de positions entre position_arrivee et position_depart
        qui représente un plus court chemin entre les deux positions
    """
    liste=[position_arrivee]
    le_calque=fabrique_le_calque(le_plateau,position_depart)
    if get(le_calque,position_arrivee) == None:
        return []
    while position_arrivee != position_depart:
        pos_mini=position_arrivee
        voisin=voisins(le_plateau,position_arrivee)
        for element in voisin:
            if get(le_calque,element)+1==get(le_calque,position_arrivee) :
                pos_mini=element
        liste.append(pos_mini)
        position_arrivee = pos_mini
    liste.pop()
    return liste
    



print(fabrique_chemin(le_plateau,(4,5),(8,8)))

def deplace_fantome(le_plateau, fantome, personnage):
    """déplace le FANTOME sur le plateau vers le personnage en prenant le chemin le plus court

    Args:
        le_plateau (plateau): un plateau de jeu
        fantome (tuple): la position du fantome sur le plateau
        personnage (tuple): la position du personnage sur le plateau

    Returns:
        [tuple]: la nouvelle position du FANTOME
    """
    if personnage == fantome:
        return personnage
    if personnage!= None and fantome!=None:
        chemin_court=fabrique_chemin(le_plateau,personnage,fantome)
        print(chemin_court)
        
        if len(chemin_court) == 1:
            if personnage == (fantome[0],fantome[1]+1):
                nv_pos=(fantome[0],fantome[1]+1)
                matrice.set_val(le_plateau,nv_pos[0],nv_pos[1],FANTOME)
                matrice.set_val(le_plateau,fantome[0],fantome[1],COULOIR)

            if personnage == (fantome[0],fantome[1]-1):
                nv_pos=(fantome[0],fantome[1]-1)
                matrice.set_val(le_plateau,nv_pos[0],nv_pos[1],FANTOME)
                matrice.set_val(le_plateau,fantome[0],fantome[1],COULOIR)
                
            if personnage == (fantome[0]+1,fantome[1]):
                nv_pos=(fantome[0]+1,fantome[1])
                matrice.set_val(le_plateau,nv_pos[0],nv_pos[1],FANTOME)
                matrice.set_val(le_plateau,fantome[0],fantome[1],COULOIR)
        
            if personnage == (fantome[0]-1,fantome[1]):
                nv_pos=(fantome[0]-1,fantome[1])
                matrice.set_val(le_plateau,nv_pos[0],nv_pos[1],FANTOME)
                matrice.set_val(le_plateau,fantome[0],fantome[1],COULOIR)
            return personnage
        
        if len(chemin_court) >= 1:
            if get(le_plateau,(chemin_court[1][0],chemin_court[1][1])) == PERSONNAGE:
                return "attrapé"
            matrice.set_val(le_plateau,chemin_court[1][0],chemin_court[1][1],3)
            matrice.set_val(le_plateau,fantome[0],fantome[1],0)
            return chemin_court[1]
    return False


print(deplace_fantome(le_plateau, (8, 8), (0, 0)))