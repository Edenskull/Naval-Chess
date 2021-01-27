board = []

lettres = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
chiffres = [8, 7, 6, 5, 4, 3, 2, 1]


class Case:
    def __init__(self, piece=None):
        self.piece = piece

    def display(self):
        if self.piece is not None:
            return self.piece.display()
        return ' '

    def empty_piece(self):
        self.piece = None

    def set_piece(self, piece):
        self.piece = piece

    def get_piece(self):
        return self.piece


class Piece:
    def __init__(self, equipe: str):
        self.equipe = equipe


class Pion(Piece):
    def __init__(self, equipe: str):
        super().__init__(equipe)

    def display(self):
        if self.equipe == "Blanc":
            return 'p'
        else:
            return 'P'

    def possible_move(self, current_x, current_y):
        move_array = []
        if self.equipe == "Blanc":
            try:
                if board[current_y + 1][current_x].get_piece() is None:
                    move_array.append(lettres[current_x] + str(chiffres[current_y + 1]))
            except IndexError:
                pass
            try:
                if board[current_y + 2][current_x].get_piece() is None:
                    move_array.append(lettres[current_x] + str(chiffres[current_y + 2]))
            except IndexError:
                pass
            try:
                test_piece = board[current_y + 1][current_x + 1].get_piece()
                if test_piece is not None:
                    if test_piece.equipe == "Noir":
                        move_array.append(lettres[current_x + 1] + str(chiffres[current_y + 1]))
            except IndexError:
                pass
            try:
                test_piece = board[current_y + 1][current_x - 1].get_piece()
                if test_piece is not None:
                    if test_piece.equipe == "Noir":
                        move_array.append(lettres[current_x - 1] + str(chiffres[current_y + 1]))
            except IndexError:
                pass
        elif self.equipe == "Noir":
            try:
                if board[current_y - 1][current_x].get_piece() is None:
                    move_array.append(lettres[current_x] + str(chiffres[current_y - 1]))
            except IndexError:
                pass
            try:
                if board[current_y - 1][current_x].get_piece() is None:
                    move_array.append(lettres[current_x] + str(chiffres[current_y - 2]))
            except IndexError:
                pass
            try:
                test_piece = board[current_y - 1][current_x + 1].get_piece()
                if test_piece is not None:
                    if test_piece.equipe == "Blanc":
                        move_array.append(lettres[current_x + 1] + str(chiffres[current_y - 1]))
            except IndexError:
                pass
            try:
                test_piece = board[current_y - 1][current_x - 1].get_piece()
                if test_piece is not None:
                    if test_piece.equipe == "Blanc":
                        move_array.append(lettres[current_x - 1] + str(chiffres[current_y - 1]))
            except IndexError:
                pass
        return move_array


class Tour(Piece):
    def __init__(self, equipe: str):
        super().__init__(equipe)

    def display(self):
        if self.equipe == "Blanc":
            return 't'
        else:
            return 'T'

    def possible_move(self, current_x, current_y):
        move_array = []
        if self.equipe == "Blanc":
            a_equipe = "Noir"
        else:
            a_equipe = "Blanc"
        for i in range(current_x + 1, 8):
            test_piece = board[current_y][i].get_piece()
            if test_piece is None:
                move_array.append(lettres[i] + str(chiffres[current_y]))
            elif test_piece.equipe == a_equipe:
                move_array.append(lettres[i] + str(chiffres[current_y]))
                break
            elif test_piece.equipe != a_equipe:
                break
        for i in range(current_x - 1, -1, -1):
            test_piece = board[current_y][i].get_piece()
            if test_piece is None:
                move_array.append(lettres[i] + str(chiffres[current_y]))
            elif test_piece.equipe == a_equipe:
                move_array.append(lettres[i] + str(chiffres[current_y]))
                break
            elif test_piece.equipe != a_equipe:
                break
        for i in range(current_y + 1, 8):
            test_piece = board[i][current_x].get_piece()
            if test_piece is None:
                move_array.append(lettres[current_x] + str(chiffres[i]))
            elif test_piece.equipe == a_equipe:
                move_array.append(lettres[current_x] + str(chiffres[i]))
                break
            elif test_piece.equipe != a_equipe:
                break
        for i in range(current_y - 1, -1, -1):
            test_piece = board[i][current_x].get_piece()
            if test_piece is None:
                move_array.append(lettres[current_x] + str(chiffres[i]))
            elif test_piece.equipe == a_equipe:
                move_array.append(lettres[current_x] + str(chiffres[i]))
                break
            elif test_piece.equipe != a_equipe:
                break
        print(move_array)
        return move_array


class Cavalier(Piece):
    def __init__(self, equipe: str):
        super().__init__(equipe)

    def display(self):
        if self.equipe == "Blanc":
            return 'c'
        else:
            return 'C'

    def possible_move(self, current_x, current_y):
        move_array = []
        if self.equipe == "Blanc":
            a_equipe = "Noir"
        else:
            a_equipe = "Blanc"
        try:
            test_piece = board[current_y + 1][current_x + 2].get_piece()
            if test_piece is None:
                move_array.append(lettres[current_x + 2] + str(chiffres[current_y + 1]))
            elif test_piece.equipe == a_equipe:
                move_array.append(lettres[current_x + 2] + str(chiffres[current_y + 1]))
        except IndexError:
            pass
        try:
            if current_x - 1 >= 0:
                test_piece = board[current_y + 1][current_x - 2].get_piece()
                if test_piece is None:
                    move_array.append(lettres[current_x - 2] + str(chiffres[current_y + 1]))
                elif test_piece.equipe == a_equipe:
                    move_array.append(lettres[current_x - 2] + str(chiffres[current_y + 1]))
        except IndexError:
            pass
        try:
            if current_y - 1 >= 0:
                test_piece = board[current_y - 1][current_x + 2].get_piece()
                if test_piece is None:
                    move_array.append(lettres[current_x + 2] + str(chiffres[current_y - 1]))
                elif test_piece.equipe == a_equipe:
                    move_array.append(lettres[current_x + 2] + str(chiffres[current_y - 1]))
        except IndexError:
            pass
        try:
            if current_y - 1 >= 0 and current_x - 2 >= 0:
                test_piece = board[current_y - 1][current_x - 2].get_piece()
                if test_piece is None:
                    move_array.append(lettres[current_x - 2] + str(chiffres[current_y - 1]))
                elif test_piece.equipe == a_equipe:
                    move_array.append(lettres[current_x - 2] + str(chiffres[current_y - 1]))
        except IndexError:
            pass
        try:
            test_piece = board[current_y + 2][current_x + 1].get_piece()
            if test_piece is None:
                move_array.append(lettres[current_x + 1] + str(chiffres[current_y + 2]))
            elif test_piece.equipe == a_equipe:
                move_array.append(lettres[current_x + 1] + str(chiffres[current_y + 2]))
        except IndexError:
            pass
        try:
            if current_x - 1 >= 0:
                test_piece = board[current_y + 2][current_x - 1].get_piece()
                if test_piece is None:
                    move_array.append(lettres[current_x - 1] + str(chiffres[current_y + 2]))
                elif test_piece.equipe == a_equipe:
                    move_array.append(lettres[current_x - 1] + str(chiffres[current_y + 2]))
        except IndexError:
            pass
        try:
            if current_y - 2 >= 0:
                test_piece = board[current_y - 2][current_x + 1].get_piece()
                if test_piece is None:
                    move_array.append(lettres[current_x + 1] + str(chiffres[current_y - 2]))
                elif test_piece.equipe == a_equipe:
                    move_array.append(lettres[current_x + 1] + str(chiffres[current_y - 2]))
        except IndexError:
            pass
        try:
            if current_y - 2 >= 0 and current_x - 1 >= 0:
                test_piece = board[current_y - 2][current_x - 1].get_piece()
                if test_piece is None:
                    move_array.append(lettres[current_x - 1] + str(chiffres[current_y - 2]))
                elif test_piece.equipe == a_equipe:
                    move_array.append(lettres[current_x - 1] + str(chiffres[current_y - 2]))
        except IndexError:
            pass
        print(move_array)
        return move_array


class Roi(Piece):
    def __init__(self, equipe: str):
        super().__init__(equipe)

    def display(self):
        if self.equipe == "Blanc":
            return 'r'
        else:
            return 'R'

    def possible_move(self, current_x, current_y):
        move_array = []
        if self.equipe == "Blanc":
            a_equipe = "Noir"
        else:
            a_equipe = "Blanc"
        try:
            test_piece = board[current_y + 1][current_x + 1].get_piece()
            if test_piece is None:
                move_array.append(lettres[current_x + 1] + str(chiffres[current_y + 1]))
            elif test_piece.equipe == a_equipe:
                move_array.append(lettres[current_x + 1] + str(chiffres[current_y + 1]))
        except IndexError:
            pass
        try:
            if current_y - 1 >= 0 and current_x - 1 >= 0:
                test_piece = board[current_y - 1][current_x - 1].get_piece()
                if test_piece is None:
                    move_array.append(lettres[current_x - 1] + str(chiffres[current_y - 1]))
                elif test_piece.equipe == a_equipe:
                    move_array.append(lettres[current_x - 1] + str(chiffres[current_y - 1]))
        except IndexError:
            pass
        try:
            test_piece = board[current_y + 1][current_x].get_piece()
            if test_piece is None:
                move_array.append(lettres[current_x] + str(chiffres[current_y + 1]))
            elif test_piece.equipe == a_equipe:
                move_array.append(lettres[current_x] + str(chiffres[current_y + 1]))
        except IndexError:
            pass
        try:
            if current_y - 1 >= 0:
                test_piece = board[current_y - 1][current_x].get_piece()
                if test_piece is None:
                    move_array.append(lettres[current_x] + str(chiffres[current_y - 1]))
                elif test_piece.equipe == a_equipe:
                    move_array.append(lettres[current_x] + str(chiffres[current_y - 1]))
        except IndexError:
            pass
        try:
            test_piece = board[current_y][current_x + 1].get_piece()
            if test_piece is None:
                move_array.append(lettres[current_x + 1] + str(chiffres[current_y]))
            elif test_piece.equipe == a_equipe:
                move_array.append(lettres[current_x + 1] + str(chiffres[current_y]))
        except IndexError:
            pass
        try:
            if current_x - 1 >= 0:
                test_piece = board[current_y][current_x - 1].get_piece()
                if test_piece is None:
                    move_array.append(lettres[current_x - 1] + str(chiffres[current_y]))
                elif test_piece.equipe == a_equipe:
                    move_array.append(lettres[current_x - 1] + str(chiffres[current_y]))
        except IndexError:
            pass
        try:
            if current_y - 1 >= 0:
                test_piece = board[current_y - 1][current_x + 1].get_piece()
                if test_piece is None:
                    move_array.append(lettres[current_x + 1] + str(chiffres[current_y - 1]))
                elif test_piece.equipe == a_equipe:
                    move_array.append(lettres[current_x + 1] + str(chiffres[current_y - 1]))
        except IndexError:
            pass
        try:
            if current_x - 1 >= 0:
                test_piece = board[current_y + 1][current_x - 1].get_piece()
                if test_piece is None:
                    move_array.append(lettres[current_x - 1] + str(chiffres[current_y + 1]))
                elif test_piece.equipe == a_equipe:
                    move_array.append(lettres[current_x - 1] + str(chiffres[current_y + 1]))
        except IndexError:
            pass
        print(move_array)
        return move_array


class Fou(Piece):
    def __init__(self, equipe: str):
        super().__init__(equipe)

    def display(self):
        if self.equipe == "Blanc":
            return 'f'
        else:
            return 'F'

    def possible_move(self, current_x, current_y):
        move_array = []
        if self.equipe == "Blanc":
            a_equipe = "Noir"
        else:
            a_equipe = "Blanc"
        iteration = 1
        for i in range(current_x + 1, 8):
            try:
                test_piece = board[current_y + iteration][i].get_piece()
                if test_piece is None:
                    move_array.append(lettres[i] + str(chiffres[current_y + iteration]))
                elif test_piece.equipe == a_equipe:
                    move_array.append(lettres[i] + str(chiffres[current_y + iteration]))
                    break
                elif test_piece.equipe != a_equipe:
                    break
            except IndexError:
                break
            iteration += 1
        iteration = 1
        for i in range(current_x + 1, 8):
            try:
                if current_y - iteration >= 0:
                    test_piece = board[current_y - iteration][i].get_piece()
                    if test_piece is None:
                        move_array.append(lettres[i] + str(chiffres[current_y - iteration]))
                    elif test_piece.equipe == a_equipe:
                        move_array.append(lettres[i] + str(chiffres[current_y - iteration]))
                        break
                    elif test_piece.equipe != a_equipe:
                        break
            except IndexError:
                pass
            iteration += 1
        iteration = 1
        for i in range(current_x - 1, -1, -1):
            try:
                test_piece = board[current_y + iteration][i].get_piece()
                if test_piece is None:
                    move_array.append(lettres[i] + str(chiffres[current_y + iteration]))
                elif test_piece.equipe == a_equipe:
                    move_array.append(lettres[i] + str(chiffres[current_y + iteration]))
                    break
                elif test_piece.equipe != a_equipe:
                    break
            except IndexError:
                pass
            iteration += 1
        iteration = 1
        for i in range(current_x - 1, -1, -1):
            try:
                if current_y - iteration >= 0:
                    test_piece = board[current_y - iteration][i].get_piece()
                    if test_piece is None:
                        move_array.append(lettres[i] + str(chiffres[current_y - iteration]))
                    elif test_piece.equipe == a_equipe:
                        move_array.append(lettres[i] + str(chiffres[current_y - iteration]))
                        break
                    elif test_piece.equipe != a_equipe:
                        break
            except IndexError:
                pass
            iteration += 1
        print(move_array)
        return move_array


class Dame(Piece):
    def __init__(self, equipe: str):
        super().__init__(equipe)

    def display(self):
        if self.equipe == "Blanc":
            return 'd'
        else:
            return 'D'

    def possible_move(self, current_x, current_y):
        move_array = []
        if self.equipe == "Blanc":
            a_equipe = "Noir"
        else:
            a_equipe = "Blanc"
        iteration = 1
        for i in range(current_x + 1, 8):
            try:
                test_piece = board[current_y + iteration][i].get_piece()
                if test_piece is None:
                    move_array.append(lettres[i] + str(chiffres[current_y + iteration]))
                elif test_piece.equipe == a_equipe:
                    move_array.append(lettres[i] + str(chiffres[current_y + iteration]))
                    break
                elif test_piece.equipe != a_equipe:
                    break
            except IndexError:
                break
            iteration += 1
        iteration = 1
        for i in range(current_x + 1, 8):
            try:
                if current_y - iteration >= 0:
                    test_piece = board[current_y - iteration][i].get_piece()
                    if test_piece is None:
                        move_array.append(lettres[i] + str(chiffres[current_y - iteration]))
                    elif test_piece.equipe == a_equipe:
                        move_array.append(lettres[i] + str(chiffres[current_y - iteration]))
                        break
                    elif test_piece.equipe != a_equipe:
                        break
            except IndexError:
                pass
            iteration += 1
        iteration = 1
        for i in range(current_x - 1, -1, -1):
            try:
                test_piece = board[current_y + iteration][i].get_piece()
                if test_piece is None:
                    move_array.append(lettres[i] + str(chiffres[current_y + iteration]))
                elif test_piece.equipe == a_equipe:
                    move_array.append(lettres[i] + str(chiffres[current_y + iteration]))
                    break
                elif test_piece.equipe != a_equipe:
                    break
            except IndexError:
                pass
            iteration += 1
        iteration = 1
        for i in range(current_x - 1, -1, -1):
            try:
                if current_y - iteration >= 0:
                    test_piece = board[current_y - iteration][i].get_piece()
                    if test_piece is None:
                        move_array.append(lettres[i] + str(chiffres[current_y - iteration]))
                    elif test_piece.equipe == a_equipe:
                        move_array.append(lettres[i] + str(chiffres[current_y - iteration]))
                        break
                    elif test_piece.equipe != a_equipe:
                        break
            except IndexError:
                pass
            iteration += 1
        for i in range(current_x + 1, 8):
            test_piece = board[current_y][i].get_piece()
            if test_piece is None:
                move_array.append(lettres[i] + str(chiffres[current_y]))
            elif test_piece.equipe == a_equipe:
                move_array.append(lettres[i] + str(chiffres[current_y]))
                break
            elif test_piece.equipe != a_equipe:
                break
        for i in range(current_x - 1, -1, -1):
            test_piece = board[current_y][i].get_piece()
            if test_piece is None:
                move_array.append(lettres[i] + str(chiffres[current_y]))
            elif test_piece.equipe == a_equipe:
                move_array.append(lettres[i] + str(chiffres[current_y]))
                break
            elif test_piece.equipe != a_equipe:
                break
        for i in range(current_y + 1, 8):
            test_piece = board[i][current_x].get_piece()
            if test_piece is None:
                move_array.append(lettres[current_x] + str(chiffres[i]))
            elif test_piece.equipe == a_equipe:
                move_array.append(lettres[current_x] + str(chiffres[i]))
                break
            elif test_piece.equipe != a_equipe:
                break
        for i in range(current_y - 1, -1, -1):
            test_piece = board[i][current_x].get_piece()
            if test_piece is None:
                move_array.append(lettres[current_x] + str(chiffres[i]))
            elif test_piece.equipe == a_equipe:
                move_array.append(lettres[current_x] + str(chiffres[i]))
                break
            elif test_piece.equipe != a_equipe:
                break
        print(move_array)
        return move_array


def init_board():
    for i in range(8):
        ligne = []
        for j in range(8):
            ligne.append(Case())
        board.append(ligne)
    # Board Blanc
    board[0][0].set_piece(Tour("Blanc"))
    board[0][1].set_piece(Cavalier("Blanc"))
    board[0][2].set_piece(Fou("Blanc"))
    board[0][3].set_piece(Dame("Blanc"))
    board[0][4].set_piece(Roi("Blanc"))
    board[0][5].set_piece(Fou("Blanc"))
    board[0][6].set_piece(Cavalier("Blanc"))
    board[0][7].set_piece(Tour("Blanc"))
    board[1][0].set_piece(Pion("Blanc"))
    board[1][1].set_piece(Pion("Blanc"))
    board[1][2].set_piece(Pion("Blanc"))
    board[1][3].set_piece(Pion("Blanc"))
    board[1][4].set_piece(Pion("Blanc"))
    board[1][5].set_piece(Pion("Blanc"))
    board[1][6].set_piece(Pion("Blanc"))
    board[1][7].set_piece(Pion("Blanc"))
    # Board Noir
    board[7][0].set_piece(Tour("Noir"))
    board[7][1].set_piece(Cavalier("Noir"))
    board[7][2].set_piece(Fou("Noir"))
    board[7][3].set_piece(Dame("Noir"))
    board[7][4].set_piece(Roi("Noir"))
    board[7][5].set_piece(Fou("Noir"))
    board[7][6].set_piece(Cavalier("Noir"))
    board[7][7].set_piece(Tour("Noir"))
    board[6][0].set_piece(Pion("Noir"))
    board[6][1].set_piece(Pion("Noir"))
    board[6][2].set_piece(Pion("Noir"))
    board[6][3].set_piece(Pion("Noir"))
    board[6][4].set_piece(Pion("Noir"))
    board[6][5].set_piece(Pion("Noir"))
    board[6][6].set_piece(Pion("Noir"))
    board[6][7].set_piece(Pion("Noir"))


def print_board():
    print(['/', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])
    iteration = 8
    for row in board:
        row_array = list()
        row_array.append(str(iteration))
        for case in row:
            row_array.append(case.display())
        print(row_array)
        iteration -= 1


def check_end():
    end_array = list()
    for row in board:
        for case in row:
            current = case.get_piece()
            if current is None:
                continue
            else:
                end_array.append(current.equipe)
    blanc = end_array.count("Blanc")
    noir = end_array.count("Noir")
    if blanc == 0:
        return "Noir"
    elif noir == 0:
        return "Blanc"
    else:
        return True


def game():
    player = "Blanc"
    while check_end():
        print_board()
        wrong_input = True
        print(f"Joueur {player} joue.")
        while wrong_input:
            origin = input("Choisi une case : ")
            split_origin = list(origin)
            if split_origin[0].lower() not in lettres:
                print("La case n'existe pas.")
                continue
            elif int(split_origin[1]) not in chiffres:
                print("La case n'existe pas.")
                continue
            current_piece = board[chiffres.index(int(split_origin[1]))][lettres.index(split_origin[0].lower())].get_piece()
            if current_piece is None:
                print("Case Vide")
                continue
            if current_piece.equipe != player:
                print("C'est pas ta pièce")
                continue
            to = input("Vers Où : ")
            split_to = list(to)
            if split_to[0].lower() not in lettres:
                print("La case n'existe pas.")
                continue
            elif int(split_to[1]) not in chiffres:
                print("La case n'existe pas.")
                continue
            if to.lower() in current_piece.possible_move(lettres.index(split_origin[0].lower()), chiffres.index(int(split_origin[1]))):
                board[chiffres.index(int(split_origin[1]))][lettres.index(split_origin[0].lower())].empty_piece()
                board[chiffres.index(int(split_to[1]))][lettres.index(split_to[0].lower())].set_piece(current_piece)
                wrong_input = False
            else:
                print("Bad Move")
        if player == "Blanc":
            player = "Noir"
        else:
            player = "Blanc"


if __name__ == '__main__':
    init_board()
    game()
