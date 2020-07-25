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

  def doAction(self, action, **kwargs):
    action_method = getattr(self, action.method.__name__)
    if action_method:
      action_method(**kwargs)
    
  def move(self, dx, dy):
    self.location_x += dx
    self.location_y += dy
  def moveNorth(self):
    self.move(dx = 0, dy = -1)
    pause("You head north...")
  def moveEast(self):
    self.move(dx = 1, dy = 0)
    pause("You head east...")
  def moveSouth(self):
    self.move(dx = 0, dy = 1)
    pause("You head south...")
  def moveWest(self):
    self.move(dx = -1, dy = 0)
    pause("You head west...")
      
  def getHelp(self):
    print(f"*************************************\n"
          f"* Basic Controls                    *\n"
          f"* go   -> move to a different room  *\n"
          f"* i    -> view inventory            *\n"
          f"* take -> pick up an item           *\n"
          f"* look -> inspect a feature closely *\n"
          f"*************************************")
    pause("Press enter to close...")
  
  def printInv(self):
    print("Inventory:")
    if len(self.inventory) > 0:
      for item in self.inventory:
        print(item)
    else:
      print("=> empty")
    pause("Press enter to close...")
    
  def getItem(self, item, room):
    pause(f"You reach out and take the {item.name}.")
    item.getItem(self)
    room.dropItem(item)
  
  def interact(self, feature):
    pause(f"You look closer at the {feature.tag}...")
    feature.interact(self)
  
  def discoverItem(self, item, feature):
    pause(f"You see -{item.name}- in the {feature.tag}.")
    # feature should drop item
    feature.dropItem(item)
    feature.room.findItem(item)

  def unlockRoom(self, room):
    # if you have the item, unlock the room!
    for item in self.items:
      if item.tag == key and item.code == room.code:
        # unlock the room
        pass
    pass