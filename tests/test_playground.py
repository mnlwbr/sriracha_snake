"""
Tests for the playground class:

- after creating the Playground objet it has the correct size attribute
- food should be inside the plathund size
- add_random_food puts the food in random positions
- food is not placed on obstacles(boundaries)
- is_obstacle for a coordinate inside gives true
- 

"""

from unittest.mock import MagicMock
from spicy_snake.playground import Playground
from unittest.mock import MagicMock
import random


def test_create():
    """ceating a PLaygeound object works"""
    p = Playground(10, 11)
    assert p.size == (10, 11)
    

def test_is_obstacle():
    """
    Check if position is an obstacle
    - is obstacle fo a coordinate inside gives False
    - is obstacke for a coordinate at the boundary gives True
    """
    p = Playground(5,6)
    
    # inside the playing field p
    assert p.is_obstacle((3,3)) is False
    
    # outside the playing field p
    assert p.is_obstacle((-1,-1)) is True

    # top left corner
    assert p.is_obstacle((0,6)) is True

    # bottom left corner
    assert p.is_obstacle((0,0)) is True


def test_add_food():
    """"food should be inside the playground"""
    p = Playground(5,6)

    p.add_food((3,3))
    assert p.food == (3, 3)

    p.add_food((0,0))
    assert p.food is None

def test_add_foo_boundary_sequence():
    """Food is deleted if an invalid position is given"""
    p = Playground(5,6)

    p.add_food((3,2))
    assert p.food is not None

    p.add_food((0,0))
    assert p.food is None

def test_add_random_food():
    """"put food in random positions"""
    p = Playground(5,6)
    p.add_random_food() # Checks is added to the playground
    assert p.food is not None


def test_add_random_food_mock():
    """"Hijack the random function to produce a predictable output"""
    p = Playground(5,6)
    mm = MagicMock(return_value = 4)
    random.randint = mm
    p.add_random_food()
    assert p.food == (4,4)
    assert mm.call_count == 2