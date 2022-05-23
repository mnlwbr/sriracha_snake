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



# feature: the snake is moving in all 4 directions
def test_move_left():
    position = (5, 5) # x, y
    new_position = move(position, 'left')
    assert new_position == (4, 5)
    
