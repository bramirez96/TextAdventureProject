from helpers import pause, prompt, borderpr, clear
import story
import books
import items as itemLib

# More Specific Naming for Imported Values

featDef = story.defaults["features"]

# BASE FEATURES


class Feature:
    def __init__(self,
                 room,      # features need to know what room they're in for full functionality
                 desc,      # block of text to print out at beginning of interaction
                 intro,     # sentence or two added to room intro. should have a default
                 tag,       # single word lowercase descriptor for cli
                 items=[]  # optional list of items found in the feature
                 ):
        self.room = room
        self.tag = tag.lower()
        self.desc = desc
        self.intro = intro
        self.items = items

    def interact(self, player):
        # all actions are dispatched through the player class
        # each feature should hve unique interactions
        raise NotImplementedError()

    def dropItem(self, item):
        self.items.remove(item)


class Bookshelf(Feature):
    def __init__(self, room, data):
        self.books = []
        for book_key in data["books"]:
            self.books.append(getattr(books, book_key))
        desc = data["desc"]
        intro = data["intro"]
        self.items = data["items"]
        super().__init__(room, desc, intro, tag="bookshelf")

    def interact(self, player):
        # need to be able to see the bookshelf and interact ->
        # interaction should display the available books and an input
        # input should select which book to read <- EASTER EGGS?
        clear()
        choice = 0
        if len(self.books) > 1:
            borderpr(self.desc)
            for i, book in enumerate(self.books):
                print(f"{i + 1}: {book.title}")
            print(f"n: I don't want to read")
            usr_input = prompt()
            if (usr_input != "n"):
                choice = int(usr_input) - 1
            else:
                choice = -1
        elif len(self.books) == 1:
            borderpr(self.desc)
            usr_input = prompt(
                f"Would you like to read \"{self.books[0].title}\"? (y/n)")
            if usr_input == "n":
                choice = -1
        else:
            borderpr(self.desc)
            prompt("There are no books on the shelf...")
            return

        if choice == -1:
            pause("You don't feel like reading right now...")
            pass
        else:
            self.books[choice].interact(player)


class Book(Feature):
    def __init__(self,
                 room,
                 title, author, text,  # specific book info
                 desc=featDef["book"]["desc"],
                 intro="You see a book.",
                 items=[]):
        self.title = title
        self.author = author
        self.text = text
        super().__init__(room=room, desc=desc, intro=intro, items=items, tag="book")

    def __str__(self):
        # initialize helpful variables for printing
        box_length = 0
        dots = "..."
        blanks = ""
        borders = ""
        the_title = f"- {self.title} -"

        # get max line length and initialize properly-sized dividers
        for line in self.text.splitlines():
            if len(line) > box_length:
                box_length = len(line)
        dotline = f"= {dots:^{box_length}s} =\n"
        blankline = f"= {blanks:{box_length}s} =\n"
        for x in range(box_length + 4):
            borders += "="

        # create book readout in newString
        newString = borders + "\n"                         # add top border
        newString += f"= {the_title:^{box_length}s} =\n"   # add title
        newString += f"= {self.author:^{box_length}s} =\n"  # add author
        newString += dotline                               # add dotted line
        for i, line in enumerate(self.text.splitlines()):
            # ignoring first line of text block (which is blank)
            # add each individual text line with the proper proper length
            newString = newString + f"= {line:<{box_length}s} =\n"
        newString += dotline  # add dots
        newString += borders  # add border
        return newString     # return text readout

    def interact(self, player):
        pause(message="You reach for the book...")  # pause for immersion
        clear()
        print(self)  # print out neatly formatted book and then pause
        pause()
        pause("You put the book down.")  # pause for immersion


# Story Specific Features

class MagicMirror(Feature):
    def __init__(self, room,
                 items=[]):
        self.count = 0
        self.story = story.zones["apartment"]["bathroom"]["features"]["mirror"]
        super().__init__(room,
                         desc=self.story["desc"][self.count],
                         intro=self.story["intro"][self.count],
                         items=items, tag="mirror")

    def interact(self, player):
        clear()
        borderpr(self.desc)
        pause()
        self.count += 1
        if self.count == 3:
            clear()
            borderpr(self.story["fallingText"])
            player.victory = True
            pause(end=True)
        else:
            self.desc = self.story["desc"][self.count]
            self.intro = self.story["intro"][self.count]


class GenericSink(Feature):
    def __init__(self,
                 room,
                 desc=featDef["sink"]["desc"],
                 intro=featDef["sink"]["intro"],
                 items=[]):
        super().__init__(room, desc, intro, tag="sink", items=items)

    def interact(self, player):
        clear()
        borderpr(self.desc)
        pause()
