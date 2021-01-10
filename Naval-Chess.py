import random

liste_bateaux = [] # Liste de tes Objets Bateau (La class juste en dessous)
lettres = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"] # Liste des lettres disponibles sur ton plateau
bateaux_size = [5, 4, 3, 3, 2, 2] # Tous les Bateau de l'IA (le chiffre représente la taille de 2 à 5) si tu veux ajouter un bateau tu ajoutes un chiffre


class Bateau: # Class bateau
    def __init__(self, pos, mode): # Initialisation de l'objet c'est la qu'il prend ces positions et son mode (vertical, horizontal)
        self.pos = pos # Tableau de position
        self.mode = mode # 0 ou 1 selon vertical ou horizontal
        self.touched = [] # les positions touchés pas le joueur
        self.killed = False # si le bateau est dead

    def check_touched(self, pos): # ici tu regardes si le bateau est touché par la position indiqué par l'utilisateur dans game
        if not self.killed:
            if pos in self.pos:
                self.touched.append(pos)
                print("Touché")
                self.check_killed()
                return True
            else:
                return False

    def check_killed(self): # Ici tu regardes si le bateau est dead
        if len(self.touched) == len(self.pos):
            print("Coulé")
            self.killed = True

    def is_killed(self): # cette fonction c'est pour eviter de lag
        if len(self.touched) == len(self.pos):
            return True
        else:
            return False


def setup(): # tu setup la position random de tes bateaux ici
    global_pos = [] # ce tableau contient toutes les pos deja utilisées par tes bateaux
    for isize in bateaux_size: # tu parcours ton tableau de taille de bateau
        check_pass = True
        while check_pass:
            check_pass = True
            modec = random.randint(0, 1) # random du mode vertical ou horizontal
            current_pos = []
            # si le bateau est à l'horizontal
            if modec == 0:
                chiffrec1 = random.randint(0, 9)
                rand_int = random.randint(0, 9)
                indexc1 = rand_int
                lettrec1 = lettres[rand_int]
                if lettrec1 + str(chiffrec1) in global_pos:
                    current_pos.clear()
                    rand_int = -1
                else:
                    check_pass = False
                if not check_pass:
                    current_pos.append(lettrec1 + str(chiffrec1))
                    global_pos.append(lettrec1 + str(chiffrec1))
                    if indexc1 > 4:
                        for iterate in range(isize-1):
                            rand_int -= 1
                            if lettres[rand_int] + str(chiffrec1) in global_pos:
                                current_pos.clear()
                                check_pass = True
                                del global_pos[-(iterate + 1):]
                                break
                            else:
                                check_pass = False
                            current_pos.append(lettres[rand_int] + str(chiffrec1))
                            global_pos.append(lettres[rand_int] + str(chiffrec1))
                    elif 0 <= indexc1 <= 4:
                        for iterate in range(isize-1):
                            if lettres[rand_int] + str(chiffrec1) in global_pos:
                                current_pos.clear()
                                check_pass = True
                                del global_pos[-(iterate + 1):]
                                break
                            else:
                                check_pass = False
                            rand_int += 1
                            current_pos.append(lettres[rand_int] + str(chiffrec1))
                            global_pos.append(lettres[rand_int] + str(chiffrec1))
            # si le bateau est à la vertical
            else:
                chiffrec1 = random.randint(0, 9)
                indexc1 = chiffrec1
                rand_int = random.randint(0, 9)
                lettrec1 = lettres[rand_int]
                if lettrec1 + str(chiffrec1) in global_pos:
                    current_pos.clear()
                    rand_int = -1
                else:
                    check_pass = False
                if not check_pass:
                    current_pos.append(lettrec1 + str(chiffrec1))
                    global_pos.append(lettrec1 + str(chiffrec1))
                    if indexc1 > 4:
                        for iterate in range(isize-1):
                            chiffrec1 -= 1
                            if lettres[rand_int] + str(chiffrec1) in global_pos:
                                current_pos.clear()
                                del global_pos[-(iterate + 1):]
                                check_pass = True
                                break
                            else:
                                check_pass = False
                            current_pos.append(lettres[rand_int] + str(chiffrec1))
                            global_pos.append(lettres[rand_int] + str(chiffrec1))
                    elif 0 <= indexc1 <= 4:
                        for iterate in range(isize-1):
                            chiffrec1 += 1
                            if lettres[rand_int] + str(chiffrec1) in global_pos:
                                current_pos.clear()
                                del global_pos[-(iterate + 1):]
                                check_pass = True
                                break
                            else:
                                check_pass = False
                            current_pos.append(lettres[rand_int] + str(chiffrec1))
                            global_pos.append(lettres[rand_int] + str(chiffrec1))
            if not check_pass:
                liste_bateaux.append(Bateau(current_pos, modec))

    for i in liste_bateaux:
        print(i.__dict__)


def print_board(board): # fonction pour afficher ton tableau simplement
    for k in board:
        print(k)


def check_win(): # fonction pour savoir si le joueur à gagné
    count = 0
    for bateau in liste_bateaux:
        if bateau.is_killed():
            count += count
    if count == len(bateaux_size):
        return True
    else:
        return False


def game(): # fonction qui permet de dérouler le jeu dans le bon ordre
    player_guess = [] # tableau de toutes les position deja ecrite par le joueur
    board = [
        ['/', "A", "B", "C", "D", "E", "F", "G", "H", "I", "J"],
        ['0', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['1', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['2', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['3', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['4', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['5', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['6', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['7', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['9', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ]
    setup()
    while not check_win():
        print_board(board)
        wrong_input = True
        while wrong_input:
            current_pos = input("Guess Position : ")
            current_pos = list(current_pos)
            if len(current_pos) == 2:
                try:
                    row = int(current_pos[1])
                except TypeError:
                    wrong_input = True
                    continue
                if current_pos[0].lower() in lettres and 0 <= row <= 9:
                    current_pos = "".join(current_pos).lower()
                    if current_pos in player_guess:
                        print("Tu as déjà donné cette position")
                        wrong_input = True
                    else:
                        check = False
                        for bateau in liste_bateaux:
                            check = bateau.check_touched(current_pos)
                            if check:
                                current_pos = list(current_pos)
                                col = lettres.index(current_pos[0])
                                row = int(current_pos[1])
                                board[row + 1][col + 1] = "X"
                                break
                        if not check:
                            current_pos = list(current_pos)
                            col = lettres.index(current_pos[0])
                            row = int(current_pos[1])
                            board[row + 1][col + 1] = "O"
                            print("Manqué")
                        wrong_input = False
                else:
                    print("Position non valide")
                    wrong_input = True
            else:
                wrong_input = True
    print("You win!")


if __name__ == '__main__':
    game()
