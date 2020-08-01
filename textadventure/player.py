import items
import world
from helpers import pause, prompt


class Player:
    def __init__(self):
        self.inventory = []
        self.hp = 100
        self.location_x, self.location_y = world.starting_position
        self.victory = False

    def isAlive(self):
        return self.hp > 0

    def doAction(self, action, **kwargs):
        action_method = getattr(self, action.method.__name__)
        if action_method:
            action_method(**kwargs)

    def move(self, dx, dy, room):
        if room.isLocked:
            # check if we need to unlock it or restrict access
            if room.counter == 0:
                room.increment()
                pause("The door is locked.")
            else:
                pause("You need to unlock the door.")
            return False
        else:
            self.location_x += dx
            self.location_y += dy
            return True

    def moveNorth(self, room):
        if self.move(dx=0, dy=-1, room=room):
            pause("You head north...")

    def moveEast(self, room):
        if self.move(dx=1, dy=0, room=room):
            pause("You head east...")

    def moveSouth(self, room):
        if self.move(dx=0, dy=1, room=room):
            pause("You head south...")

    def moveWest(self, room):
        if self.move(dx=-1, dy=0, room=room):
            pause("You head west...")

    def unlockDoor(self, room):
        if room.isLocked:
            hasKey = False
            for item in self.inventory:
                if item.tag == "key" and item.code == room.code:
                    room.unlock()
                    pause("You turn the key and hear the lock open.")
                    hasKey = True
                    self.consumeItem(item)
                    break
            if not hasKey:
                pause("You don't seem to have the right key...")
        else:
            pause("You've already unlocked this door.")

    def getHelp(self):
        print(f"********************************************\n"
              f"* Basic Controls                           *\n"
              f"* go     -> move to a different room       *\n"
              f"* i      -> view inventory                 *\n"
              f"* take   -> pick up an item                *\n"
              f"* look   -> inspect a feature closely      *\n"
              f"* unlock -> unlock a locked door or object *\n"
              f"********************************************")
        pause("Press enter to close...")

    def printInv(self):
        print("Inventory:")
        if len(self.inventory) > 0:
            for item in self.inventory:
                print(item)
        else:
            print("=> empty")
        pause("Press enter to close...")

    def getItem(self, item, room):
        pause(f"You reach out and take the {item.name}.")
        item.getItem(self)
        room.dropItem(item)

    def interact(self, feature):
        pause(f"You look closer at the {feature.tag}...")
        feature.interact(self)

    def discoverItem(self, item, feature):
        pause(f"You see -{item.name}- in the {feature.tag}.")
        # feature should drop item
        feature.dropItem(item)
        feature.room.findItem(item)

    def consumeItem(self, item):
        # this function is going to mainly be used for keys for now,
        # but is helpful to keep inventory clear when any single-use
        # item is expended
        self.inventory.remove(item)
