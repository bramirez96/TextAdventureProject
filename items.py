class Item:
  def __init__(self, name, tag, desc, intro):
    self.name = name
    self.tag = tag
    self.desc = desc
    self.intro = intro
  def __str__(self):
    return f"=> {self.name} - {self.desc}"
  def getItem(self, player):
    player.inventory.append(self)
  def getIntro(self):
    return self.intro

# so the way this is set up, items pass keyword arguments to constructor only
# intro is passed in positionally as first arg

class Gum(Item):
  def __init__(self, intro):
    super().__init__(name="Gum",
                     tag="gum", 
                     desc="a single stick of gum.", 
                     intro=intro)

class Screwdriver(Item):
  def __init__(self, intro):
    super().__init__(name="Screwdriver",
                     tag="screwdriver",
                     desc="this could come in handy", 
                     intro=intro)