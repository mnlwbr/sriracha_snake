import curses


""" LEFT = (-1, 0)
RIGHT = (1, 0)
UP = (0, -1)
DOWN = (0, 1)

KEY_COMMANDS = {97: LEFT, 100: RIGHT, 119: UP, 115: DOWN}

# prepare the screen
screen = curses.initscr()
curses.start_color()
curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
curses.curs_set(0)
curses.noecho()
curses.raw()
screen.keypad(False)

win = curses.newwin(80, 25, 0, 0)
win.nodelay(True)
 """

# defensive code: validity checks on input data
VALID_DIRECTIONS = {'up','right','down','left'}

def move(current_position, direction):
    assert direction in VALID_DIRECTIONS
    x, y = current_position

    #
    if type(x) != int or type(y) != int:
        raise Exception("x and y have to be integers")

    # code that does the calculations
    if direction is 'right':
        new_position = x+1, y
    
    elif direction is 'up':
        new_position = x, y+1
    
    elif direction is 'down':
        new_position = x, y-1
    
    else:
        new_position = x-1, y

    return(new_position)



""" 
def game_loop(screen):
    x, y = 5, 5

    # draw
    screen.clear()
    screen.addch(y, x, "O", curses.color_pair(1))
    win.refresh()
    screen.refresh()

    while True:

        char = win.getch()
        direction = KEY_COMMANDS.get(char)
        if direction:
            dx, dy = direction
            x += dx
            y += dy

            # draw
            screen.clear()
            screen.addch(y, x, "O", curses.color_pair(1))
            win.refresh()
            screen.refresh()


if __name__ == "__main__":

    curses.wrapper(game_loop)
    curses.endwin()
 """