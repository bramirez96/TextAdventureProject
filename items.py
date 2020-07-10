class Item:
  def __init__(self, name, desc, intro):
    self.name = name
    self.desc = desc
    self.intro = intro
  def __str__(self):
    return f"=> {self.name} - {self.desc}"
  def getItem(self, player):
    player.inventory.append(self)
  def getIntro(self):
    return self.intro

class Gum(Item):
  def __init__(self, intro):
    super().__init__(name="gum", 
                     desc="a single stick of gum.", 
                     intro=intro)

class Screwdriver(Item):
  def __init__(self, intro):
    super().__init__(name="screwdriver", 
                     desc="this could come in handy", 
                     intro=intro)