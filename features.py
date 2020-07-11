from helpers import pause, prompt, borderpr, clear
import story
import items

# BASE FEATURES 

class Feature:
  def __init__(self, 
               desc,      # block of text to print out at beginning of interaction 
               intro,     # sentence or two added to room intro. should have a default
               tag,       # single word lowercase descriptor for cli
               items = [] # optional list of items found in the feature
               ):
    self.tag   = tag.lower()
    self.desc  = desc
    self.intro = intro
    self.items = items
  def interact(self, player):
    # all actions are dispatched through the player class
    # each feature should hve unique interactions
    raise NotImplementedError()

class Bookshelf(Feature):
  def __init__(self,
               desc  = story.interactions["bookshelfDEF"], # default
               intro = "You see a bookshelf.", # default
               books = [], #default to no books
               items = []):
    self.books = books
    super().__init__(desc, intro, items=items, tag="bookshelf")
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
    else:
      borderpr(self.desc)
      usr_input = prompt(f"Would you like to read \"{self.books[0].title}\"? (y/n)")
      if usr_input == "n":
        choice = -1
    if choice == -1:
      pause("You don't feel like reading right now...")
      pass
    else:
      self.books[choice].interact(player)

class Book(Feature):
  def __init__(self, title, author, text, # specific book info
               desc = story.interactions["bookDEF"], 
               intro = "You see a book.", 
               items = []):
    self.title = title
    self.author = author
    self.text = text
    super().__init__(desc, intro, items=items, tag="book")
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
    newString += f"= {self.author:^{box_length}s} =\n" # add author
    newString += dotline                               # add dotted line    
    for i, line in enumerate(self.text.splitlines()):
      # ignoring first line of text block (which is blank)
      # add each individual text line with the proper proper length
      if i != 0:
         newString = newString + f"= {line:<{box_length}s} =\n"
    newString += dotline # add dots
    newString += borders # add border
    return newString     # return text readout
  def interact(self, player):
    pause(message = "You reach for the book...") # pause for immersion
    clear()
    print(self) # print out neatly formatted book and then pause
    pause()
    pause("You put the book down.") # pause for immersion
  
  
# Story Specific Features
class MagicMirror(Feature):
  def __init__(self,
               desc = story.interactions["mirror1"], 
               intro = story.interactions["mirrorIntro1"], 
               items = []):
    self.count = 1
    super().__init__(desc, intro, items=items, tag="mirror")
  def interact(self, player):
    clear()
    borderpr(self.desc)
    pause()
    self.count += 1
    if self.count == 4:
      clear()
      borderpr(story.interactions["falling"])
      player.victory = True
      pause(end=True)
    else:
      self.desc = story.interactions[f"mirror{self.count}"]
      self.intro = story.interactions[f"mirrorIntro{self.count}"]
      