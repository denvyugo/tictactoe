import pytest

from tictactoe import (check_integers_input, check_elements_quantity,
                       check_elements_in_range, check_input,
                       clear_field, fill_index_of_coordinates,
                       SIZE, set_field_state, print_field, get_mark_turn,
                       check_position_occupied, set_position, check_winner)

def test_check_digits():
    """check if inputs are integer digits through a space"""
    assert check_integers_input('3 4') == True
    assert check_integers_input('on s') == False
    assert check_integers_input('1 l') == False
    assert check_integers_input('') == False
    assert check_integers_input('2 52 1 005') == True
    assert check_integers_input('2.0 0.0') == False

def test_check_elements_quantity():
    """check if quantity of elements in inputs is equal length"""
    assert check_elements_quantity('3 4') == True
    assert check_elements_quantity('on s') == True
    assert check_elements_quantity('1 l', length=2) == True
    assert check_elements_quantity('') == False
    assert check_elements_quantity('2 52 1 005', 4) == True
    assert check_elements_quantity('2.0 0.0', 3) == False
    
def test_check_elements_in_range():
    """check if all elements in inputs are integer in range [low, high]"""
    assert check_elements_in_range('3 4') == False
    assert check_elements_in_range('1 2', low=1, high=3) == True
    assert check_elements_in_range('') == False
    assert check_elements_in_range('2 52 1 5', low=0, high=100) == True
    assert check_elements_in_range('2 0') == False

def test_check_input():
    """check inputs on conditions:
    two elements are integers in range [1, 3]"""
    assert check_input('3 4') == 'Coordinates should be from 1 to 3!'
    assert check_input('on s') == 'You should enter numbers!'
    assert check_input('1 l') == 'You should enter numbers!'
    assert check_input('') == 'You should enter numbers!'
    assert check_input('2 52 1 005') == 'You should enter numbers!'
    assert check_input('2.0 0.0') == 'You should enter numbers!'
    assert check_input('1 2') == None

def test_clear_field():
    """fill a field of empty marks '_'"""
    clear_field()
    from tictactoe import field_state
    assert field_state == '_' * SIZE ** 2

def test_fill_index_of_coordinates():
    """fill a dictionary[tuple(column, row): index_of_field_state_string]"""
    fill_index_of_coordinates()
    from tictactoe import index_of_coordinates
    assert len(index_of_coordinates) == SIZE ** 2
    assert index_of_coordinates[(1, 1)] == 6
    assert index_of_coordinates[(2, 1)] == 7
    assert index_of_coordinates[(3, 1)] == 8
    assert index_of_coordinates[(1, 2)] == 3
    assert index_of_coordinates[(2, 2)] == 4
    assert index_of_coordinates[(3, 2)] == 5
    assert index_of_coordinates[(1, 3)] == 0
    assert index_of_coordinates[(2, 3)] == 1
    assert index_of_coordinates[(3, 3)] == 2

def test_position_occupied():
    """check if position in field_state string is not equal empty mark '_'"""
    marks = '_XXOO_OX_'
    message_occupied = 'This cell is occupied! Choose another one!'
    set_field_state(marks)
    from tictactoe import field_state
    print()
    print_field()
    assert field_state == marks
    assert check_position_occupied((1, 1)) == message_occupied
    assert check_position_occupied((1, 2)) == message_occupied
    assert check_position_occupied((1, 3)) is None
    assert check_position_occupied((2, 1)) == message_occupied
    assert check_position_occupied((2, 2)) == message_occupied
    assert check_position_occupied((2, 3)) == message_occupied
    assert check_position_occupied((3, 1)) is None
    assert check_position_occupied((3, 2)) is None
    assert check_position_occupied((3, 3)) == message_occupied
    set_position((1, 3), 'X')
    from tictactoe import field_state
    print()
    print_field()

def test_check_winner():
    """check what the mark is winner and return it or None"""
    marks = '_XXOO_OX_'
    message_occupied = 'This cell is occupied! Choose another one!'
    set_field_state(marks)
    from tictactoe import field_state
    print()
    print_field()
    assert field_state == marks
    set_position((1, 3), 'X')
    from tictactoe import field_state
    print()
    print_field()
    message_win = 'X wins'
    assert check_winner('X') == message_win

def test_get_mark():
    """chet get_mark_turn function"""
    marks = '_XXOO_OX_'
    set_field_state(marks)
    from tictactoe import field_state
    print()
    print_field()
    assert get_mark_turn() == 'X'

    
    
