import items, world
from helpers import pause

class Player:
  def __init__(self):
    self.inventory = []
    self.hp = 100
    self.location_x, self.location_y = world.starting_position
    self.victory = False
    
  def isAlive(self):
    return self.hp > 0

  def printInv(self):
    print("Inventory:")
    if len(self.inventory) > 0:
      for item in self.inventory:
        print(item)
    else:
      print("=> empty")
    pause("Press enter to close...")
      
  def move(self, dx, dy):
    self.location_x += dx
    self.location_y += dy
  
  def getHelp(self):
    print(f"*************************************\n"
          f"* Basic Controls                    *\n"
          f"* go   -> move to a different room  *\n"
          f"* i    -> view inventory            *\n"
          f"* get  -> pick up an item           *\n"
          f"* look -> inspect a feature closely *\n"
          f"*************************************")
    pause("Press enter to close...")

  def interact(self, feature):
    pause(f"You look closer at the {feature.name}...")
    feature.interact(self)
  def getItem(self, item, room):
    pause(f"You reach out and take the {item.name}.")
    item.getItem(self)
    room.dropItem(item)
  
  def moveNorth(self):
    self.move(dx = 0, dy = -1)
  def moveEast(self):
    self.move(dx = 1, dy = 0)
  def moveSouth(self):
    self.move(dx = 0, dy = 1)
  def moveWest(self):
    self.move(dx = -1, dy = 0)
    
    
  def doAction(self, action, **kwargs):
    action_method = getattr(self, action.method.__name__)
    if action_method:
      action_method(**kwargs)