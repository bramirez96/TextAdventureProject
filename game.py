import world
from player import Player

def play():
  world.load_tiles()
  player = Player()
  while player.isAlive and not player.victory:
    # run game loop
    print(world._world)
    input("orasdasd")
    pass

play()