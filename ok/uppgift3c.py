#Anton Gefvert antge210, Aleksi Evansson aleev379
#3. Bearbetning av listor
#
#Uppgift 3C

"""
vikho394: OK!
Bra modulär lösning, bra uppdelning!
Ni har dock rader som är längre än 79 tecken. De bör göras radbrytningar :) 
om man ska vara petig. 

Hade ett litet tips i nearest_piece också. 
"""

import math
#Create empty board
board = {}

def reset_board():
    """ Empties the board """
    board.clear()


def isfree(x, y):
    """ Checks whether the tile at (x, y) is empty) """
    return not (x,y) in board


def place_piece(x, y, player):
    """ Places "player" at tile (x, y) if it is free """
    if not isfree(x,y):
        return False
    else:
        board[(x,y)] = player
        return True


def get_piece(x, y):
    """ Returns the name of the owner of the tile (x, y) """
    return board[(x,y)] if (x,y) in board else False


def remove_piece(x, y):
    """ Empties tile (x, y) """
    if isfree(x,y):
        return False
    else:
        del board[(x,y)]
        return True


def move_piece(from_x, from_y, to_x, to_y):
    """ Moves the piece from (from_x, from_y) to (x, y) if possible """
    if isfree(from_x, from_y):
        return False
    player = get_piece(from_x, from_y)
    if place_piece(to_x, to_y, player):
        del board[(from_x, from_y)]
        return True
    return False


def count(orientation, index, player):
    """ Counts the tiles owned by "player" in row/column("orientation") "index" """
    if orientation == "row": 
        orientation_index = 0
    else:
        orientation_index = 1
    count = 0
    for elem in board:
        if elem[orientation_index] == index and board[elem] == player:
            count += 1
    return count
        

def nearest_piece(x, y):
    """ Returns the coordinates for the tile closest to (x, y) """
    shortest_dist = -1
    shortest_dist_elem = ()

    """
    Ni kan använda tupel syntaxen som ni har sätt tidigare

    for x,y in board

    då får ni tupelelementen direkt istället :)
    """
    for elem in board:
        elem_x = elem[0]
        elem_y = elem[1]
        dist = math.sqrt((elem_x - x)**2 + (elem_y - y)**2)
        if dist < shortest_dist or shortest_dist == -1:
            shortest_dist = dist
            shortest_dist_elem = (elem_x, elem_y)
    return shortest_dist_elem

if __name__  == "__main__":

    # Tests interpret
    assert isfree(500, 100)
    assert place_piece(500, 100, "spelare1")
    assert place_piece(1, 100, "spelare2")
    assert not place_piece(500, 100, "spelare2")
    assert place_piece(500, 200, "spelare2")
    assert not isfree(500, 100)
    assert get_piece(500, 100) == "spelare1"
    assert not get_piece(666,666)
    assert remove_piece(500, 100)
    assert not remove_piece(1, 1)
    assert isfree(500, 100)
    assert move_piece( 500, 200, 500, 100 )
    assert get_piece(500, 100) == "spelare2"
    assert count("row", 500, "spelare2") == 1
    assert count("column", 100, "spelare2") == 2
    assert nearest_piece(500, 105) == (500, 100)
