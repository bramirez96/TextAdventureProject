import world
from story import messages
from player import Player
from helpers import pause, borderpr, prompt, clear


def play():
    world.load_tiles()
    player = Player()
    clear()
    borderpr(messages["loadingScreen"])
    pause()

    while player.isAlive and not player.victory:
        # run game loop
        clear()
        room = world.tile_exists(player.location_x, player.location_y)
        borderpr(room.intro_text())
        available_actions = room.available_actions()
        # print("Choose an action:\n")
        # for action in available_actions:
        #   print(f">> {action}")
        isValid = False
        action_input = prompt()
        for action in available_actions:
            if action_input == action.hotkey:
                player.doAction(action, **action.kwargs)
                isValid = True
                break
        if not isValid:
            pause("You're not sure how you'd do that...")


play()