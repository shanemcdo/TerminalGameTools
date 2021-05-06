import colorama
from msvcrt import getch

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

def give_options(options: [any, ...], cursor: str = '>', prompt: str = None, starting_index: int = 0) -> (int, any):
    """
    colorama.init must be called for this function to work
    Allows the user to select from a list of options visually using arrow keys/wasd and enter/space
    :options: a list of options that will be displayed
    :cursor: the cursor that will be printed before the current option
    :prompt: the prompt to be printed before the the menu
    :starting_index: the index the cursor will start at
    :returns: a tuple containing the index of the selected item and the value
    """
    cursor_len = len(cursor)
    options_len = len(options)
    empty_cursor = ' ' * cursor_len
    current_index = starting_index
    if prompt is None:
        prompt = 'Please select an option:'
    print(prompt)
    while 1:
        for i, item in enumerate(options):
            print(cursor if current_index == i else empty_cursor, item)
        ch = getch().lower()
        if ch == b'w':
            current_index -= 1
            if current_index < 0:
                current_index += options_len
        elif ch == b's':
            current_index += 1
            if current_index > options_len:
                current_index %= options_len
        elif ch == b' ' or ch == b'\r':
            break
        elif ord(ch) == 224:
            key_code = ord(getch())
            if key_code == 72: # up arrow
                current_index -= 1
                if current_index < 0:
                    current_index += options_len
            elif key_code == 80: # down arrow
                current_index += 1
                if current_index > options_len:
                    current_index %= options_len
        move_cursor_rel(0, -options_len)
    return current_index, options[current_index]
