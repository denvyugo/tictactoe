import pytest

from tictactoe import (SIZE, set_field_state, get_mark_turn,
                       print_field, fill_index_of_coordinates,
                       find_win_by_rows, find_win_by_cols,
                       find_win_by_main_diagonal,
                       find_win_by_other_diagonal,
                       get_coordinates_by_index)

def test_find_win_by_rows():
    """check find win by rows"""
    fill_index_of_coordinates()
    from tictactoe import index_of_coordinates
    print(index_of_coordinates)
    marks = '_XXOO_OX_'
    set_field_state(marks)
    from tictactoe import field_state
    print()
    print_field()
    mark = get_mark_turn()
    assert find_win_by_rows(mark) == (1, 3)
    marks = '___X_OXXO'
    set_field_state(marks)
    from tictactoe import field_state
    print()
    print_field()
    mark = get_mark_turn()
    assert find_win_by_cols(mark) == (3, 3)
    marks = '___OX_XO_'
    set_field_state(marks)
    from tictactoe import field_state
    print()
    print_field()
    mark = get_mark_turn()
    assert find_win_by_main_diagonal(mark) == (3, 3)
    marks = '_X__OXX_O'
    set_field_state(marks)
    from tictactoe import field_state
    print()
    print_field()
    mark = get_mark_turn()
    assert find_win_by_other_diagonal(mark) == (1, 3)

def test_coordinates_by_index():
    assert get_coordinates_by_index(0) == (1, 3)
    assert get_coordinates_by_index(1) == (2, 3)
    assert get_coordinates_by_index(2) == (3, 3)
    assert get_coordinates_by_index(3) == (1, 2)
    assert get_coordinates_by_index(4) == (2, 2)
    assert get_coordinates_by_index(5) == (3, 2)
    assert get_coordinates_by_index(6) == (1, 1)
    assert get_coordinates_by_index(7) == (2, 1)
    assert get_coordinates_by_index(8) == (3, 1)
