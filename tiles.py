import items, actions, world, features, books, story

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
    moves.append(actions.Help())
    return moves
  def dropItem(self, item):
    raise NotImplementedError()

class ItemRoom(Room):
  def __init__(self, x, y, item):
    super().__init__(x, y)
    self.item = item
  def available_actions(self):
    moves = [*super().available_actions(), actions.GetItem(self.item)]
    return moves

class FeatureRoom(Room):
  def __init__(self, x, y, feature):
    super().__init__(x, y)
    self.feature = feature
  def available_actions(self):
    # this includes all base actions for a standard room and whatever you need for this one
    moves = [*super().available_actions(), actions.Interact(self.feature)]
    return moves

class ComboRoom(Room):
  def __init__(self, x, y, features = [], items = []):
    super().__init__(x, y)
    self.features = features
    self.items = items
  def available_actions(self):
    # includes all base actions for a tile
    moves = super().available_actions()
    
    # needs to include hotkey for ALL features in room
    for feature in self.features:
      moves.append(actions.Interact(feature))
    
    # and ALL items
    for item in self.items:
      moves.append(actions.GetItem(item, self))
    
    # returns those actions correctly
    return moves
  def dropItem(self, item):
    # remove the item from the room when player picks it up
    self.items.remove(item)
  def addItem(self, item):
    self.items.append(item)
    
class AptBed(ComboRoom):
  def __init__(self, x, y):
    super().__init__(x, y, features = [features.Bookshelf(
      books.poeTalesPoems,
      books.firstStep
    )])
  def intro_text(self):
    return story.roomIntro["AptBed"]
  def modify_player(self, player):
    pass

class AptLR(FeatureRoom):
  def __init__(self, x, y,
               feature = features.Bookshelf(
                 books.aliceInWonderland,
                 books.furiouslyHappy,
                 books.madnessBipolar,
                 desc = story.interactions["bookshelfApt"]
                )):
    super().__init__(x, y, feature)
  def intro_text(self):
    return story.roomIntro["AptLR"]

class AptKit(ComboRoom):
  def __init__(self, x , y):
    super().__init__(x, y, items=[items.Gum()])
  def intro_text(self):
    return story.roomIntro["AptKit"]

class AptBath(ComboRoom):
  def __init__(self, x, y):
    super().__init__(x, y, features = [features.MagicMirror()])
  def intro_text(self):
    return story.roomIntro["AptBath"]
  def modify_player(self, player):
    player.victory = True

class BookTest(FeatureRoom):
  def __init__(self, x, y, feature = books.firstStep):
    super().__init__(x, y, feature)
  def intro_text(self):
    return "You're in a room. There's a book on the table."

class Road(Room):
  def __init__(self, x, y):
    super().__init__(x, y)
  def intro_text(self):
    return "You are on an empty stretch of road"

class ItemTest(ItemRoom):
  def __init__(self, x, y, item = items.Screwdriver()):
    super().__init__(x, y, item)
  def intro_text(self):
    return "You see a screwdriver behind a rock or something idk"

class ComboTest(ComboRoom):
  def __init__(self, x, y):
    super().__init__(x, y, features =[], items=[items.Screwdriver(), items.Gum()])
  def intro_text(self):
    return "This is a test of the combo room."


class IFTest(ComboRoom):
  def __init__(self, x, y):
    super().__init__(x, y, features=[features.DeskWithScrewdiver()])
  def intro_text(self):
    return "You see a desk in the corner"
  def available_actions(self):
    # includes all base actions for a tile
    moves = self.adjacent_moves()
    moves.append(actions.ViewInventory())
    moves.append(actions.Help())
    
    # needs to include hotkey for ALL features in room
    for feature in self.features:
      if len(feature.items) > 0:
        for item in feature.items:
          moves.append(actions.FindItem(feature, item, self))
      else:
        moves.append(actions.Interact(feature))
    
    # and ALL items
    for item in self.items:
      moves.append(actions.GetItem(item, self))
    
    # returns those actions correctly
    return moves
  