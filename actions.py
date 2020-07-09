from player import Player
import tiles

class Action:
  def __init__(self, method, name, hotkey, **kwargs):
    self.method = method
    self.name   = name
    self.hotkey = hotkey
    self.kwargs = kwargs
  def __str__(self):
    return f"{self.hotkey}: {self.name}"
  
class MoveNorth(Action):
  def __init__(self):
    super().__init__(method=Player.moveNorth, name="Move north", hotkey="n")
class MoveEast(Action):
  def __init__(self):
    super().__init__(method=Player.moveEast, name="Move east", hotkey="e")
class MoveSouth(Action):
  def __init__(self):
    super().__init__(method=Player.moveSouth, name="Move south", hotkey="s")
class MoveWest(Action):
  def __init__(self):
    super().__init__(method=Player.moveWest, name="Move west", hotkey="w")
class ViewInventory(Action):
  def __init__(self):
    super().__init__(method=Player.printInv, name="View inventory", hotkey="i")
class GetItem(Action):
  def __init__(self, item):
    super().__init__(method=tiles.ItemRoom.modify_player, name="Pickup item", hotkey="p")