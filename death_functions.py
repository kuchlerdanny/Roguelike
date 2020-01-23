import tcod as libtcod
from render_functions import RenderOrder
from game_states import GameStates  

def kill_player(player):
    player.char = '%'
    player.color = libtcod.dark_red

    return 'You died!', GameStates.PLAYER_DEAD

def kill_monster(monster):
    death_message = '{0} dies'.format(monster.name.capitalize())

    monster.char = '%'
    monster.color = libtcod.dark_red
    monster.blocks = False
    monster.render_order = RenderOrder.CORPSE   
    monster.fighter = None
    monster.ai = None
    monster.name = monster.name + ' carcas'

    return death_message