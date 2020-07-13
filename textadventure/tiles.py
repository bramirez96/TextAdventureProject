import actions, world, story,\
  features as featureLib, items as itemLib
from books import books

class Room:
  def __init__(self, x, y, intro):
    self.x = x
    self.y = y
    self.intro = intro
    self.north = None
    self.east  = None
    self.south = None
    self.west  = None
  def intro_text(self):
    raise NotImplementedError()
  def modify_player(self, player):
    raise NotImplementedError()
  def adjacent_moves(self):
    moves = []
    north = world.tile_exists(self.x, self.y - 1)
    east  = world.tile_exists(self.x + 1, self.y)
    south = world.tile_exists(self.x, self.y + 1)
    west  = world.tile_exists(self.x - 1, self.y)
    if north:
      moves.append(actions.MoveNorth())
      self.north = north
    if east:
      moves.append(actions.MoveEast())
      self.east = east
    if south:
      moves.append(actions.MoveSouth())
      self.south = south
    if west:
      moves.append(actions.MoveWest())
      self.west = west
    return moves
  def available_actions(self):
    moves = self.adjacent_moves()
    moves.append(actions.ViewInventory())
    moves.append(actions.Help())
    return moves
  def dropItem(self, item):
    raise NotImplementedError()
  def findItem(self, item):
    raise NotImplementedError()


class ComboRoom(Room):
  def __init__(self, x, y,
               features = [], 
               items = [],
               intro = story.defaults["rooms"]["intro"]):
    super().__init__(x, y, intro=intro)
    self.features = features
    self.items = items
  def available_actions(self):
    # includes all base actions for a tile
    moves = super().available_actions()
    
    # needs to append hotkeys for ALL features in room
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
  def findItem(self, item):
    # add item to room when it;s discovered in a feature
    self.items.append(item)
  def intro_text(self):
    # run this function purely to load adjacent tiles so that
    # their intros are included
    self.adjacent_moves()
    newText = "\n"
    for feature in self.features:
      newText += "\n" + feature.intro
    for item in self.items:
      newText += "\n" + item.intro
    if self.north:
      newText += f"\n\nTo the north {self.north.intro}"
    if self.east:
      newText += f"\n\nTo the east {self.east.intro}"
    if self.south:
      newText += f"\n\nTo the south {self.south.intro}"
    if self.west:
      newText += f"\n\nTo the west {self.west.intro}"
    return newText
    
class AptBed(ComboRoom):
  def __init__(self, x, y):
    super().__init__(x, y,
                     features = [featureLib.Bookshelf(
                       room  = self,
                       books = [featureLib.Book(room=self, **books["alice"])],
                       desc  = story.zones["apartment"]["bedroom"]["features"]["bookshelf"]["desc"],
                       intro = story.zones["apartment"]["bedroom"]["features"]["bookshelf"]["intro"]
                     )],
                     intro = story.zones["apartment"]["bedroom"]["intro"]
                     )
  def intro_text(self):
    return story.zones["apartment"]["bedroom"]["desc"] + super().intro_text()
  def modify_player(self, player):
    pass

class AptLR(ComboRoom):
  def __init__(self, x, y):
    super().__init__(x, y, 
                     features = [
                       featureLib.Bookshelf(
                         room=self,
                         books=[
                           featureLib.Book(room=self, **books["furiouslyHappy"]),
                           featureLib.Book(room=self, **books["madnessBipolar"]),
                           featureLib.Book(room=self, **books["poeTales"]),
                           featureLib.Book(room=self, **books["firstStep"])
                         ],
                         desc  = story.zones["apartment"]["livingRoom"]["features"]["bookshelf"]["desc"],
                         intro = story.zones["apartment"]["livingRoom"]["features"]["bookshelf"]["intro"],
                       )
                     ],
                     intro = story.zones["apartment"]["livingRoom"]["intro"],
                     )
  def intro_text(self):
    return story.zones["apartment"]["livingRoom"]["desc"] + super().intro_text()

class AptKit(ComboRoom):
  def __init__(self, x , y):
    super().__init__(x, y,
                     features = [featureLib.GenericSink(self)],
                     items=[itemLib.Gum(story.zones["apartment"]["kitchen"]["items"]["gum"]["intro"])],
                     intro=story.zones["apartment"]["kitchen"]["intro"]
                     )
  def intro_text(self):
    return story.zones["apartment"]["kitchen"]["desc"] + super().intro_text()

class AptBath(ComboRoom):
  def __init__(self, x, y):
    super().__init__(x, y, 
                     features = [featureLib.MagicMirror(room=self)],
                     intro=story.zones["apartment"]["bathroom"]["intro"][0])
  def intro_text(self):
    curCount = self.features[0].count
    self.intro = story.zones["apartment"]["bathroom"]["intro"][curCount]
    text = story.zones["apartment"]["bathroom"]["desc"][curCount] + super().intro_text()
    return text
