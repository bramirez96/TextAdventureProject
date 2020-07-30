from player import Player
import tiles


class Action:
    def __init__(self, method, name, hotkey, **kwargs):
        self.method = method
        self.name = name
        self.hotkey = hotkey
        self.kwargs = kwargs

    def __str__(self):
        return f"{self.hotkey}: {self.name}"


class MoveNorth(Action):
    def __init__(self):
        super().__init__(method=Player.moveNorth,
                         name="Move north",
                         hotkey="go north")


class UnlockNorth(Action):
    def __init__(self, room):
        super().__init__(method=Player.unlockNorth,
                         name="Unlock north",
                         hotkey="unlock north",
                         room=room)


class MoveEast(Action):
    def __init__(self):
        super().__init__(method=Player.moveEast,
                         name="Move east",
                         hotkey="go east")


class UnlockEast(Action):
    def __init__(self, room):
        super().__init__(method=Player.unlockEast,
                         name="Unlock east",
                         hotkey="unlock east",
                         room=room)


class MoveSouth(Action):
    def __init__(self):
        super().__init__(method=Player.moveSouth,
                         name="Move south",
                         hotkey="go south")


class UnlockSouth(Action):
    def __init__(self, room):
        super().__init__(method=Player.unlockSouth,
                         name="Unlock south",
                         hotkey="unlock south",
                         room=room)


class MoveWest(Action):
    def __init__(self):
        super().__init__(method=Player.moveWest,
                         name="Move west",
                         hotkey="go west")


class UnlockWest(Action):
    def __init__(self, room):
        super().__init__(method=Player.unlockWest,
                         name="Unlock west",
                         hotkey="unlock west",
                         room=room)


class Help(Action):
    def __init__(self):
        super().__init__(method=Player.getHelp,
                         name="Help",
                         hotkey="help")


class ViewInventory(Action):
    def __init__(self):
        super().__init__(method=Player.printInv,
                         name="View inventory",
                         hotkey="i")


class GetItem(Action):
    def __init__(self, item, room):
        super().__init__(method=Player.getItem,
                         name="Pickup item",
                         hotkey=f"take {item.tag}",
                         item=item,
                         room=room)


class Interact(Action):
    def __init__(self, feature):
        super().__init__(method=Player.interact,
                         name=f"Look at {feature.tag}",
                         hotkey=f"look {feature.tag}",
                         feature=feature)


class DiscoverItem(Action):
    def __init__(self, item, feature):
        super().__init__(method=Player.discoverItem,
                         name=f"Discover the {item.tag}",
                         hotkey=f"search {feature.tag}",
                         item=item,
                         feature=feature)
