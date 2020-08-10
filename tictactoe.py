# write your code here
from random import randint
from typing import Optional, Tuple


SIZE = 3
field_state = ''
index_of_coordinates = {}


def check_integers_input(inputs: str) -> bool:
    """check if inputs are integer digits through a space"""
    if inputs:
        return all(map(lambda x: x.isdecimal(), inputs.split()))
    else:
        return False


def check_elements_quantity(inputs: str, length=2) -> bool:
    """check if quantity of elements in inputs is equal length"""
    return len(inputs.split()) == length


def check_elements_in_range(inputs: str, low=1, high=3) -> bool:
    """check if all elements in inputs are integer in range [low, high]"""
    if inputs:
        return all(map(lambda x: low <= int(x) <= high, inputs.split()))
    else:
        return False


def check_input(inputs: str) -> Optional[str]:
    """check inputs on conditions:
    two elements are integers in range [1, 3]"""
    if not check_elements_quantity(inputs):
        return 'You should enter numbers!'
    if not check_integers_input(inputs):
        return 'You should enter numbers!'
    if not check_elements_in_range(inputs):
        return 'Coordinates should be from 1 to 3!'


def check_start_command(commands: str) -> bool:
    """check if start command include two player parameters"""
    players = ('user', 'easy', 'medium', 'hard')
    if commands.startswith('start'):
        parameters = commands.split()
        if len(parameters) == 3:
            valid_command = parameters[1] in players and\
                            parameters[2] in players
        else:
            valid_command = False
    else:
        valid_command = False
    return valid_command


def gen_coordinates():
    """generator for coordinates (column: int, row: int): tuple by rows"""
    max_elements = SIZE ** 2
    row = SIZE
    col = 1
    for _ in range(max_elements):
        if col > SIZE:
            col = 1
            row -= 1
        yield col, row
        col += 1


def fill_index_of_coordinates():
    """fill a dictionary[(column, row), index_of_field_state_string]"""
    max_elements = SIZE ** 2
    coordinates = gen_coordinates()
    for n in range(max_elements):
        index_of_coordinates[next(coordinates)] = n


def get_coordinates_by_index(index: int) -> Tuple[int, int]:
    """get coordinates by index of cell in field state string"""
    # check if index over the field size
    if 0 <= index < len(field_state):
        coordinates = dict(zip(index_of_coordinates.values(),
                               index_of_coordinates.keys()))
        return coordinates[index]


def clear_field():
    """fill a field of empty marks '_'"""
    global field_state
    field_state = '_' * SIZE ** 2


def set_field_state(field_marks: str):
    """set an initial field_state by string"""
    global field_state
    if len(field_marks) != SIZE ** 2:
        pass
    field_state = field_marks


def check_position_occupied(coordinates: Tuple[int, int]) -> Optional[str]:
    """check if position in field_state string is not equal empty mark '_'"""
    mark_index = index_of_coordinates.get(coordinates)
    if mark_index is None:
        pass
    if field_state[mark_index] != '_':
        return 'This cell is occupied! Choose another one!'


def get_mark_turn() -> str:
    """get the mark of next move"""
    number_x = field_state.count('X')
    number_o = field_state.count('O')
    if number_o == number_x:
        mark = 'X'
    else:
        mark = 'O'
    return mark


def set_position(coordinates: Tuple[int, int], mark: str):
    """set an appropriate mark to position with coordinates"""
    index = index_of_coordinates[coordinates]
    marks = list(field_state)
    marks[index] = mark
    set_field_state(''.join(marks))


def check_winner_by_rows(mark: str) -> bool:
    """check rows if the mark is winner"""
    found = 0
    for row in range(SIZE):
        found = 0
        for col in range(SIZE):
            index = index_of_coordinates[(col + 1, row + 1)]
            if field_state[index] == mark:
                found += 1
            else:
                break
        if found == SIZE:
            break
    return found == SIZE


def check_winner_by_cols(mark: str) -> bool:
    """check columns if the mark is winner"""
    found = 0
    for col in range(SIZE):
        found = 0
        for row in range(SIZE):
            index = index_of_coordinates[(col + 1, row + 1)]
            if field_state[index] == mark:
                found += 1
            else:
                break
        if found == SIZE:
            break
    return found == SIZE


def check_winner_main_diagonal(mark: str) -> bool:
    """check main diagonal if the mark is winner"""
    found = 0
    for element in range(SIZE):
        index = index_of_coordinates[(element + 1, element + 1)]
        if field_state[index] == mark:
            found += 1
        else:
            break
    return found == SIZE


def check_winner_other_diagonal(mark: str) -> bool:
    """check other diagonal if the mark is winner"""
    found = 0
    for element in range(SIZE):
        index = index_of_coordinates[(element + 1, SIZE - element)]
        if field_state[index] == mark:
            found += 1
        else:
            break
    return found == SIZE


def check_winner(mark: str) -> Optional[str]:
    """check what the mark is winner and return it or None"""
    win = False
    if not win:
        win = check_winner_by_rows(mark)
    if not win:
        win = check_winner_by_cols(mark)
    if not win:
        win = check_winner_main_diagonal(mark)
    if not win:
        win = check_winner_other_diagonal(mark)
    if win:
        return f'{mark} wins'


def check_draw() -> Optional[str]:
    """check if all cell are occupied"""
    if field_state.count('_') == 0:
        return 'Draw'


def print_field():
    """print field with marks by field_state"""
    print('-' * 3 * SIZE)
    index = 0
    for row in range(SIZE):
        row_elements = ' '.join(
            field_state[index:index + SIZE]).replace('_', ' ')
        row_string = f'| {row_elements} |'
        index = index + SIZE
        print(row_string)
    print('-' * 3 * SIZE)


def get_free_random_position() -> Tuple[int, int]:
    """find free cell random position"""
    while True:
        col = randint(1, SIZE)
        row = randint(1, SIZE)
        message = check_position_occupied((col, row))
        if message:
            continue
        else:
            break
    return col, row


def move_easy() -> str:
    """move easy for random coordinates, return mark"""
    print('Making move level "easy"')
    col, row = get_free_random_position()
    mark = get_mark_turn()
    set_position((col, row), mark)
    return mark


def find_win_by_rows(mark: str) -> Tuple[int, int]:
    """find if in rows has a one win move for mark"""
    row_found = 0
    row_string = []
    for row in range(SIZE):
        row_found = 0
        row_string.clear()
        for col in range(SIZE):
            index = index_of_coordinates[(col + 1, row + 1)]
            row_string.append(field_state[index])
        if row_string.count(mark) == SIZE - 1 and\
                row_string.count('_') == 1:
            row_found = row + 1
            break
    if row_found:
        # find index of free cell in row
        col_found = row_string.index('_') + 1
        return col_found, row_found


def find_win_by_cols(mark: str) -> Tuple[int, int]:
    """find if in columns has a one win move for mark"""
    col_found = 0
    col_string = []
    for col in range(SIZE):
        col_found = 0
        col_string.clear()
        for row in range(SIZE):
            index = index_of_coordinates[(col + 1, row + 1)]
            col_string.append(field_state[index])
        if col_string.count(mark) == SIZE - 1 and\
                col_string.count('_') == 1:
            col_found = col + 1
            break
    if col_found:
        # find index of free cell in row
        row_found = col_string.index('_') + 1
        return col_found, row_found


def find_win_by_main_diagonal(mark: str) -> Tuple[int, int]:
    """find if in main diagonal has a one win move for mark """
    col_string = []
    for element in range(SIZE):
        index = index_of_coordinates[(element + 1, element + 1)]
        col_string.append(field_state[index])
    if col_string.count(mark) == SIZE - 1 and \
            col_string.count('_') == 1:
        element = col_string.index('_') + 1
        return element, element


def find_win_by_other_diagonal(mark: str) -> Tuple[int, int]:
    """find if in other diagonal has a one win move for mark """
    col_string = []
    for element in range(SIZE):
        index = index_of_coordinates[(element + 1, SIZE - element)]
        col_string.append(field_state[index])
    if col_string.count(mark) == SIZE - 1 and \
            col_string.count('_') == 1:
        element = col_string.index('_') + 1
        return element, SIZE - element + 1


def find_one_win_move(mark: str) -> Tuple[int, int]:
    """find one win move for mark by rows, columns, diagonals"""
    # analyse win move by rows
    position = find_win_by_rows(mark)
    if not position:
        # analyse win move by columns
        position = find_win_by_cols(mark)
    if not position:
        # analyse win move by main diagonal
        position = find_win_by_main_diagonal(mark)
    if not position:
        # analyse win move by other diagonal
        position = find_win_by_other_diagonal(mark)
    return position


def move_medium() -> str:
    """move medium level difficulty:
    try to win when has a one winning move
    try to block opponent to win in one move"""
    # print('Making move level "medium"')
    mark = get_mark_turn()
    position = find_one_win_move(mark)
    if not position:
        if mark == 'X':
            op_mark = 'O'
        else:
            op_mark = 'X'
        position = find_one_win_move(op_mark)
    if not position:
        # random (easy) move
        position = get_free_random_position()
    set_position(position, mark)
    print('Making move level "medium"')
    return mark


def get_score_game(mark: str, turn_mark: str) -> Optional[int]:
    """calculate score of game status to user's mark"""
    game_over = False
    score_game = 0
    check_message = check_winner(turn_mark)
    if check_message:
        game_over = True
        if mark == turn_mark:
            score_game = 10
        else:
            score_game = -10
    if not game_over:
        check_message = check_draw()
        if check_message:
            game_over = True
            score_game = 0
    if game_over:
        return score_game
    else:
        return None


def minimax(mark: str, turn_mark: str) -> int:
    """recursively get a value of resulting game"""
    score_position = get_score_game(mark, turn_mark)
    if score_position is not None:
        return score_position
    else:
        step_field_state = field_state
        turn_mark = get_mark_turn()
        if mark == turn_mark:
            score_position = -1000
        else:
            score_position = 1000
        free_cells = [i for i, char in enumerate(field_state) if char == '_']
        for index in free_cells:
            coordinates = get_coordinates_by_index(index)
            set_position(coordinates, turn_mark)
            score_game = minimax(mark, turn_mark)
            if mark == turn_mark:
                if score_position < score_game:
                    score_position = score_game
            else:
                if score_position > score_game:
                    score_position = score_game
            # restore field state
            set_field_state(step_field_state)
        return score_position


def move_hard() -> str:
    """move hard: minimax algorithm"""
    mark = get_mark_turn()
    # print(f'Making move level "hard" with {mark}')
    position = ()
    # if field_state.count('_') > 7:
    #     # move random (easy)
    #     position = get_free_random_position()
    # else:
    # try one win move
    position = find_one_win_move(mark)
    if not position:
        # save current field state
        current_field_state = field_state
        # minimax algorithm
        score_position = -1000
        free_cells = [i for i, char in enumerate(field_state) if char == '_']
        for index in free_cells:
            coordinates = get_coordinates_by_index(index)
            set_position(coordinates, mark)
            score_game = minimax(mark, mark)
            if score_position < score_game:
                score_position = score_game
                position = coordinates
            # restore field state
            set_field_state(current_field_state)
    # make move
    set_position(position, mark)
    print('Making move level "hard"')
    return mark


def move_player() -> str:
    """move player: enter coordinates, return mark"""
    position = ()
    while True:
        coordinates = input('Enter the coordinates: > ')
        check_message = check_input(coordinates)
        if check_message:
            print(check_message)
            continue
        position = tuple(map(int, coordinates.split()))
        # noinspection PyTypeChecker
        check_message = check_position_occupied(position)
        if check_message:
            print(check_message)
            continue
        break
    mark = get_mark_turn()
    # noinspection PyTypeChecker
    set_position(position, mark)
    return mark


def move_user(user: str) -> str:
    """choose what user move now by user name"""
    mark = ''
    if user == 'user':
        mark = move_player()
    elif user == 'easy':
        mark = move_easy()
    elif user == 'medium':
        mark = move_medium()
    elif user == 'hard':
        mark = move_hard()
    return mark


def step_game(mark: str) -> bool:
    """check if mark win or not after move"""
    game_over = False
    print_field()
    check_message = check_winner(mark)
    if check_message:
        print(check_message)
        game_over = True
    if not game_over:
        check_message = check_draw()
        if check_message:
            print(check_message)
            game_over = True
    return game_over


def game(user1: str, user2: str):
    """tictactoe game"""
    fill_index_of_coordinates()
    # cells = input('Enter cells: > ')
    # set_field_state(cells)
    clear_field()
    print_field()
    game_over = False
    while not game_over:
        for player in (user1, user2):
            mark = move_user(player)
            game_over = step_game(mark)
            if game_over:
                break


if __name__ == '__main__':
    while True:
        command = input('Input command: > ')
        if command == 'exit':
            break
        if check_start_command(command):
            command_args = command.split()
            game(user1=command_args[1],
                 user2=command_args[2])
        else:
            print('Bad parameters!')
