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

# class ItemRoom(Room):
#   def __init__(self, x, y, item):
#     super().__init__(x, y)
#     self.item = item
#   def available_actions(self):
#     moves = [*super().available_actions(), actions.GetItem(self.item)]
#     return moves

# class FeatureRoom(Room):
#   def __init__(self, x, y, feature):
#     super().__init__(x, y)
#     self.feature = feature
#   def available_actions(self):
#     # this includes all base actions for a standard room and whatever you need for this one
#     moves = [*super().available_actions(), actions.Interact(self.feature)]
#     return moves

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
  def intro_text(self):
    newText = ""
    for item in self.items:
      newText += item.intro
    return newText
    
class AptBed(ComboRoom):
  def __init__(self, x, y):
    super().__init__(x, y, 
                     features = [features.Bookshelf(
                       books.aliceInWonderland,
                       desc = story.interactions["bsAPTBR"]
                     )])
  def intro_text(self):
    return story.roomIntro["AptBed"]
  def modify_player(self, player):
    pass

class AptLR(ComboRoom):
  def __init__(self, x, y,
               feature = [features.Bookshelf(
                 books.furiouslyHappy,
                 books.madnessBipolar,
                 books.poeTalesPoems,
                 books.firstStep,
                 desc = story.interactions["bsAPTLR"]
                )]):
    super().__init__(x, y, feature)
  def intro_text(self):
    return story.roomIntro["AptLR"]

class AptKit(ComboRoom):
  def __init__(self, x , y):
    super().__init__(x, y, items=[items.Gum(story.items["aptKitGum"])])
  def intro_text(self):
    return story.roomIntro["AptKit"] + "\n" + super().intro_text()

class AptBath(ComboRoom):
  def __init__(self, x, y):
    super().__init__(x, y, features = [features.MagicMirror()])
    self.count = 1
  def intro_text(self):
    text = story.roomIntro[f"AptBath{self.count}"]
    self.count += 1
    return text
  def modify_player(self, player):
    player.victory = True

class Road(Room):
  def __init__(self, x, y):
    super().__init__(x, y)
  def intro_text(self):
    return "You are on an empty stretch of road"
