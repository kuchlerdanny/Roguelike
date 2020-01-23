import tcod as libtcod

def handle_keys(key):
    key_char = chr(key.c)

    if key.vk == libtcod.KEY_KP8 or key.vk == libtcod.KEY_UP: # or key_char == 'k':
        return {'move': (0, -1)}
    elif key.vk == libtcod.KEY_KP2 or key.vk == libtcod.KEY_DOWN:
        return {'move': (0, 1)}
    elif key.vk == libtcod.KEY_KP4 or key.vk == libtcod.KEY_LEFT:
        return {'move': (-1, 0)}
    elif key.vk == libtcod.KEY_KP6 or key.vk == libtcod.KEY_RIGHT:
        return {'move': (1, 0)}
    elif key.vk == libtcod.KEY_KP7 or key_char == 'y':
        return {'move': (-1, -1)}
    elif key.vk == libtcod.KEY_KP9 or key_char == 'u':
        return {'move': (1, -1)}
    elif key.vk == libtcod.KEY_KP1 or key_char == 'b':
        return {'move': (-1, 1)}
    elif key.vk == libtcod.KEY_KP3 or key_char == 'n':
        return {'move': (1, 1)}

    if key.vk == libtcod.KEY_ENTER and KEY_lalt:
        #alt+enter toggles full screen
        return {'fullscreen': True}

    elif key.vk == libtcod.KEY_ESCAPE:
        #exit game
        return{'exit': True}

    #no key pressed
    return {} 