import tcod as libtcod
from game_messages import Message
from render_functions import RenderOrder
from game_states import GameStates  

def kill_player(player):
    player.char = '%'
    player.color = libtcod.dark_red

    return Message('You died!', libtcod.red), GameStates.PLAYER_DEAD

def kill_monster(monster):
    death_message = Message('{0} is dead!'.format(monster.name.capitalize()), libtcod.orange)

    monster.char = '%'
    monster.color = libtcod.dark_red
    monster.blocks = False
    monster.render_order = RenderOrder.CORPSE   
    monster.fighter = None
    monster.ai = None
    monster.name = monster.name + ' carcas'

    return death_message