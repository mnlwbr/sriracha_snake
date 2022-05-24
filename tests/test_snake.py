"""
Automated Test with pytest

The disploicne of TDD (Test-Driven-Development)

1. Write a test
2. Run the test and make sure it fails
3. Write just enough code to make the test pass
4. Run the test again and make sure it passes
5. Clean up
6. Run the tests again (regression testing)
7. Backt to step 1

also see: Uncle Bob "Clean Code Lectures"


"""
import random
import pytest
from spicy_snake.moves import move #VALID_DIRECTIONS


#TODO: also test random positions

@pytest.mark.parametrize('postion,direction,expected', [
    # data examples
    ((5,5), 'left', (4,5)),
    ((5,5), 'right', (6,5)),
    ((5,5), 'up', (5,6)),
    ((5,5), 'down', (5,4))
])
def test_move(postion, direction, expected):
    """ # feature: the snake is moving in all 4 directions"""
    assert move(postion,direction) == expected

def test_move_left_from_somewhere_else():
    position = (1, 5) # x, y
    new_position = move(position, 'left')
    assert new_position == (0, 5)

def test_move_invalid_direction():
    with pytest.raises(Exception):
        move((1,1), 'dummy')

def test_move_random():
    """test random positions"""
    for _ in range(100):
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        position = x, y
        new_position = move(position,'left')
        assert new_position == (x-1, y)

def test_move_fraction():
    """
    This is an exampl of code that is not supposed to work
    """
    position = (3.14159, 5) # x, y

    with pytest.raises(Exception): # test passes if an Exception is generatesd
        move(position, 'down')



