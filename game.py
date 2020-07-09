import world
from player import Player

def play():
  world.load_tiles()
  player = Player()
  while player.isAlive and not player.victory:
    # run game loop
    room = world.tile_exists(player.location_x, player.location_y)
    print(room.intro_text())
    available_actions = room.available_actions()
    print("Choose an action:\n")
    for action in available_actions:
      print(f">> {action}")
    action_input = input(">> ")
    for action in available_actions:
      if action_input == action.hotkey:
        player.doAction(action, **action.kwargs)
        break

if __name__ == "__main__":
  play()