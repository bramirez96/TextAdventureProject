class Item:
  def __init__(self, name, desc):
    self.name = name
    self.desc = desc
  def __str__(self):
    return f"=> {self.name} - {self.desc}"

class Gum(Item):
  def __init__(self):
    super().__init__(name="Gum", desc="A single stick of gum.")
