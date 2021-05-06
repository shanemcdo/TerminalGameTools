import colorama

def move_cursor(x: int, y: int):
    """
    colorama.init must be called for this function to work
    Uses ANSI escape codes to move the cursor to an absolute position.
    :x: the x coordinate to move to. the smallest value that will do anything is 1
    :y: the y coordinate to move to. the smallest value that will do anything is 1
    """
    print(f'\033[{y};{x}H', end='', flush=True)

def move_cursor_rel(x: int, y: int):
    """
    colorama.init must be called for this function to work
    Uses ANSI escape codes to move the cursor to a relative position
    :x: the x coordinate to move relatively
    :y: the y coordinate to move relatively
    """
    if y < 0: # y is less than 0
        print(f'\033[{abs(y)}A', end='', flush=True) # move y down
    elif y > 0: # y is more than 0
        print(f'\033[{y}B', end='', flush=True) # move abs(y) up
    if x > 0: # x is more than 0
        print(f'\033[{x}C', end='', flush=True) # move x right
    elif x < 0: # x is less than 0
        print(f'\033[{abs(x)}D', end='', flush=True) # move abs(x) left
