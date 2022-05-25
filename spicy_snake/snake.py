
from playground import Playground
import curses
from screen_helper import prepare_screen


LEFT = (-1, 0)
RIGHT = (1, 0)
UP = (0, 1)
DOWN = (0, -1)

KEY_COMMANDS = {97: LEFT, 100: RIGHT, 115: UP, 119: DOWN}



win, screen = prepare_screen()

def draw(pg,xPlayer,yPlayer):
    x = pg.size[0]
    y = pg.size[1]
    screen.clear()
    screen.addch(yPlayer, xPlayer, "O", curses.color_pair(1)) #FIXME: this is needed here? Maybe...
    for x in range(31):
        for y in range(15):
            if pg.is_obstacle((x, y)):
                screen.addch(y, x, "#", curses.color_pair(2))
    win.refresh()
    screen.refresh()
    #return(xPlayer,yPlayer)

def game_loop(screen):
    xPlayer, yPlayer = 5, 5 #FIXME: player position

    pg = Playground(30, 14) #FIXME: should this be initialized before?

    # draw
    draw(pg,xPlayer,yPlayer)

    while True:

        # move the player
        char = win.getch()
        direction = KEY_COMMANDS.get(char)
        if direction:
            dx, dy = direction
            xPlayer += dx
            yPlayer += dy

            # draw

            draw(pg,xPlayer,yPlayer)




if __name__ == "__main__":

    curses.wrapper(game_loop)
    curses.endwin()
