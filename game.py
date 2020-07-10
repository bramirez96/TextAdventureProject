import world, story
from player import Player
from helpers import pause, borderpr, prompt, clear

def play():
  world.load_tiles()
  player = Player()
  clear()
  for i in story.intro:
    borderpr(i)
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
    action_input = prompt()
    for action in available_actions:
      if action_input == action.hotkey:
        player.doAction(action, **action.kwargs)
        break

if __name__ == "__main__":
  play()