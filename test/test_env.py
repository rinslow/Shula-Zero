import numpy
from env.minesweeper import calculate_neighbors_given_a_bomb, BOMB


def test_neighbors_edge_left_top():
    empty_matrix = numpy.zeros([3, 3])
    valued_matrix = calculate_neighbors_given_a_bomb(empty_matrix, 0, 0)

    assert valued_matrix.tolist() == [[0, 1, 0],
                                      [1, 1, 0],
                                      [0, 0, 0]]


def test_neighbors_edge_mid_top():
    empty_matrix = numpy.zeros([3, 3])
    valued_matrix = calculate_neighbors_given_a_bomb(empty_matrix, 0, 1)

    assert valued_matrix.tolist() == [[1, 0, 1],
                                      [1, 1, 1],
                                      [0, 0, 0]]


def test_neighbors_edge_right_top():
    empty_matrix = numpy.zeros([3, 3])
    valued_matrix = calculate_neighbors_given_a_bomb(empty_matrix, 0, 2)

    assert valued_matrix.tolist() == [[0, 1, 0],
                                      [0, 1, 1],
                                      [0, 0, 0]]


def test_neighbors_edge_left_mid():
    empty_matrix = numpy.zeros([3, 3])
    valued_matrix = calculate_neighbors_given_a_bomb(empty_matrix, 1, 0)

    assert valued_matrix.tolist() == [[1, 1, 0],
                                      [0, 1, 0],
                                      [1, 1, 0]]


def test_neighbors_edge_mid_mid():
    empty_matrix = numpy.zeros([3, 3])
    valued_matrix = calculate_neighbors_given_a_bomb(empty_matrix, 1, 1)

    assert valued_matrix.tolist() == [[1, 1, 1],
                                      [1, 0, 1],
                                      [1, 1, 1]]


def test_neighbors_edge_right_mid():
    empty_matrix = numpy.zeros([3, 3])
    valued_matrix = calculate_neighbors_given_a_bomb(empty_matrix, 1, 2)

    assert valued_matrix.tolist() == [[0, 1, 1],
                                      [0, 1, 0],
                                      [0, 1, 1]]


def test_neighbors_edge_left_bot():
    empty_matrix = numpy.zeros([3, 3])
    valued_matrix = calculate_neighbors_given_a_bomb(empty_matrix, 2, 0)

    assert valued_matrix.tolist() == [[0, 0, 0],
                                      [1, 1, 0],
                                      [0, 1, 0]]


def test_neighbors_edge_mid_bot():
    empty_matrix = numpy.zeros([3, 3])
    valued_matrix = calculate_neighbors_given_a_bomb(empty_matrix, 2, 1)

    assert valued_matrix.tolist() == [[0, 0, 0],
                                      [1, 1, 1],
                                      [1, 0, 1]]


def test_neighbors_edge_right_bot():
    empty_matrix = numpy.zeros([3, 3])
    valued_matrix = calculate_neighbors_given_a_bomb(empty_matrix, 2, 2)

    assert valued_matrix.tolist() == [[0, 0, 0],
                                      [0, 1, 1],
                                      [0, 1, 0]]

def test_bombs_dont_get_changed():
    empty_matrix = numpy.zeros([3, 3])
    empty_matrix[0, 0] = BOMB
    valued_matrix = calculate_neighbors_given_a_bomb(empty_matrix, 1, 0)

    assert valued_matrix.tolist() == [[BOMB, 1, 0],
                                      [0,    1, 0],
                                      [1,    1, 0]]