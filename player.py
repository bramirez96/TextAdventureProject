import items, world

class Player:
  def __init__(self):
    self.inventory = []
    self.hp = 100
    self.location_x, self.location_y = world.starting_position
    self.victory = False
    
  def isAlive(self):
    return self.hp > 0

  def printInv(self):
    for item in self.inventory:
      print(f"{item}\n")
      
  def move(self, dx, dy):
    self.location_x += dx
    self.location_y += dy

  def interact(self, feature):
    feature.interact(self)
  
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