import actions, world, books, story
import features as featureLib
import items as itemLib

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
               intro = "is another room"):
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
                       room=self,
                       books=[featureLib.Book(room=self, **books.aliceInWonderland)],
                       desc = story.interactions["bsAPTBR"],
                       intro = story.featureIntros["aptBRBookshelf"]
                     )],
                     intro = "is your bedroom. You'd love to curl \n\
back up in bed right now.")
  def intro_text(self):
    return story.roomIntro["AptBed"] + super().intro_text()
  def modify_player(self, player):
    pass

class AptLR(ComboRoom):
  def __init__(self, x, y):
    super().__init__(x, y, 
                     features = [
                       featureLib.Bookshelf(
                         room=self,
                         books=[
                           featureLib.Book(room=self, **books.furiouslyHappy),
                           featureLib.Book(room=self, **books.madnessBipolar),
                           featureLib.Book(room=self, **books.poeTalesPoems),
                           featureLib.Book(room=self, **books.firstStep)
                         ],
                         desc = story.interactions["bsAPTLR"],
                         intro = story.featureIntros["aptLRBookshelf"]
                       )
                     ],
                     intro = "is your living room.")
  def intro_text(self):
    return story.roomIntro["AptLR"] + super().intro_text()

class AptKit(ComboRoom):
  def __init__(self, x , y):
    super().__init__(x, y,
                     features = [featureLib.GenericSink(self)],
                     items=[itemLib.Gum(story.items["aptKitGum"])],
                     intro="is your kitchen. When was the last time\n\
you ate? The days are starting to blur together.")
  def intro_text(self):
    return story.roomIntro["AptKit"] + super().intro_text()

class AptBath(ComboRoom):
  def __init__(self, x, y):
    super().__init__(x, y, 
                     features = [featureLib.MagicMirror(room=self)],
                     intro="is your bathroom.")
  def intro_text(self):
    curCount = self.features[0].count
    text = story.roomIntro[f"AptBath{curCount}"] + super().intro_text()
    return text

class FITest(ComboRoom):
  def __init__(self, x, y, 
               items=[], 
               intro='is a test room'):
    super().__init__(x, y, 
                     features=[featureLib.TestFeat(room=self)], 
                     items=items, intro=intro)
  def intro_text(self):
    return story.interactions["testRoomFI"] + super().intro_text()