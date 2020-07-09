import items, actions, world, features

class Room:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  def intro_text(self):
    raise NotImplementedError()
  def modify_player(self, player):
    raise NotImplementedError()
  def adjacent_moves(self):
    moves = []
    if world.tile_exists(self.x, self.y - 1):
      moves.append(actions.MoveNorth())
    if world.tile_exists(self.x + 1, self.y):
      moves.append(actions.MoveEast())
    if world.tile_exists(self.x, self.y + 1):
      moves.append(actions.MoveSouth())
    if world.tile_exists(self.x - 1, self.y):
      moves.append(actions.MoveWest())
    return moves
  def available_actions(self):
    moves = self.adjacent_moves()
    moves.append(actions.ViewInventory())
    return moves

class ItemRoom(Room):
  def __init__(self, x, y, item):
    super().__init__(x, y)
    self.item = item
  def get_item(self, player):
    player.inventory.append(self.item)
  def modify_player(self, player):
    self.get_item(player)
  def available_actions(self):
    moves = [*super().available_actions(), actions.GetItem()]

class FeatureRoom(Room):
  def __init__(self, x, y, feature):
    super().__init__(x, y)
    self.feature = feature
  def interact(self, feature):
    raise NotImplementedError()

class AptBed(Room):
  def __init__(self, x=1, y=1):
    super().__init__(x, y)
  def intro_text(self):
    return "You're in your room. LR is N"
  def modify_player(self, player):
    pass

class AptLR(FeatureRoom):
  def __init__(self, 
               x = 1, y = 0, 
               feature = features.Bookshelf(
                 features.aliceInWonderland
                )):
    super().__init__(x, y, feature)
  def intro_text(self):
    return "You're in your living room. You see a bookshelf"

class AptKit(ItemRoom):
  def __init__(self, x = 0, y = 0, item = items.Gum()):
    super().__init__(x, y, item)
  def intro_text(self):
    return "You're in your kitchen. There is gum on the table."

class AptBath(FeatureRoom):
  def __init__(self, x = 2, y = 0, 
               feature = features.MagicMirror()):
    super().__init__(x, y, feature)
  def intro_text(self):
    return "You're in your fairly standard bathroom. There's a mirror on the wall above the sink, a toilet, and a shower"