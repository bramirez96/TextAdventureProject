class Item:
  def __init__(self, name, desc):
    self.name = name
    self.desc = desc
  def __str__(self):
    return f"=> {self.name} - {self.desc}"
  def getItem(self, player):
    player.inventory.append(self)


class Gum(Item):
  def __init__(self):
    super().__init__(name="gum", desc="a single stick of gum.")

class Screwdriver(Item):
  def __init__(self):
    super().__init__(name="screwdriver", desc="this could come in handy")