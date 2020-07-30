import actions
import world
import story
import \
    features as featureLib, items as itemLib
from books import books


# Main Room Classes


class Room:
    def __init__(self, x, y, intro):
        self.x = x
        self.y = y
        self.locked = False
        self.intro = intro
        self.north = None
        self.east = None
        self.south = None
        self.west = None

    def intro_text(self):
        raise NotImplementedError()

    def modify_player(self, player):
        raise NotImplementedError()

    def adjacent_moves(self):
        moves = []
        north = world.tile_exists(self.x, self.y - 1)
        east = world.tile_exists(self.x + 1, self.y)
        south = world.tile_exists(self.x, self.y + 1)
        west = world.tile_exists(self.x - 1, self.y)
        if north:
            if north.locked:
                moves.append(actions.UnlockNorth(north))
            else:
                moves.append(actions.MoveNorth())
            self.north = north
        if east:
            if east.locked:
                moves.append(actions.UnlockEast(east))
            else:
                moves.append(actions.MoveEast())
            self.east = east
        if south:
            if south.locked:
                moves.append(actions.UnlockSouth(south))
            else:
                moves.append(actions.MoveSouth())
            self.south = south
        if west:
            if west.locked:
                moves.append(actions.UnlockWest(west))
            else:
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
    def __init__(self, x, y, data):
        self.desc = data["desc"]
        super().__init__(x, y, intro=data["intro"])
        self.features = []
        self.items = []
        for feat_name in data["features"]:
            self.features.append(getattr(featureLib, feat_name)(
                self,
                data["features"][feat_name])
            )
        for item_name in data["items"]:
            self.items.append(getattr(itemLib, item_name)(
                **data["items"][item_name]
            ))

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
        newText = "\n" + self.desc + "\n"

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


class EventRoom(ComboRoom):
    def __init__(self, x, y, data):
        super().__init__(x, y, data={
            "desc": data["desc"][0],
            "intro": data["intro"][0],
            "features": data["features"],
            "items": data["items"]
        })
        self.story = {
            "desc": data["desc"],
            "intro": data["intro"]
        }
        self.counter = 0

    def increment(self):
        self.counter += 1
        if self.counter < len(self.story["desc"]):
            self.desc = self.story["desc"][self.counter]
        if self.counter < len(self.story["intro"]):
            self.intro = self.story["intro"][self.counter]


class LockedRoom(EventRoom):
    def __init__(self, x, y, data):
        super().__init__(x, y, data)
        self.code = data["key"]
        self.locked = True

    def unlock(self):
        self.locked = False
        self.increment()


# # Zone 1: Apartment


# class AptKit(ComboRoom):
#     def __init__(self, x, y):
#         super().__init__(x, y,
#                          features=[featureLib.GenericSink(self)],
#                          items=[itemLib.Gum(
#                              story.zones["apartment"]["kitchen"]["items"]["gum"]["intro"])],
#                          intro=story.zones["apartment"]["kitchen"]["intro"]
#                          )

#     def intro_text(self):
#         return story.zones["apartment"]["kitchen"]["desc"] + super().intro_text()


# class AptBath(ComboRoom):
#     def __init__(self, x, y):
#         super().__init__(x, y,
#                          features=[featureLib.MagicMirror(room=self)],
#                          intro=story.zones["apartment"]["bathroom"]["intro"][0])

#     def intro_text(self):
#         curCount = self.features[0].count
#         self.intro = story.zones["apartment"]["bathroom"]["intro"][curCount]
#         text = story.zones["apartment"]["bathroom"]["desc"][curCount] + \
#             super().intro_text()
#         return text
