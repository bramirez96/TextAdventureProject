from helpers import pause, prompt, borderpr, clear
import story
import items

class Feature:
  def __init__(self, name):
    super().__init__()
    self.name = name
  def interact(self, player):
    raise NotImplementedError()

class ItemFeature(Feature):
  def __init__(self, name, *items):
    super().__init__(name)
    self.items = items
  def interact(self, player, room):
    raise NotImplementedError()
  # def findItem(self, item, room):
  #   room.items.append(item)
  #   self.items.remove(item)
   
class Book(Feature):
  def __init__(self, title, author, text):
    super().__init__(name="book")
    self.title = title
    self.author = author
    self.text = text
  def __str__(self):
    # initialize helpful variables for printing
    box_length = 0
    dots = "..."
    blanks = ""
    borders = ""
    
    # get max line length in specific text
    for line in self.text.splitlines():
      if len(line) > box_length:
        box_length = len(line)
    
    # creating dividers based on variable length
    dotline = f"= {dots:^{box_length}s} =\n"
    blankline = f"= {blanks:{box_length}s} =\n"
    
    # create border based on length of text
    for x in range(box_length + 4):
      borders += "="
    
    # add a border
    newString = borders + "\n"
    
    # add title and author
    the_title = f"- {self.title} -"
    newString += f"= {the_title:^{box_length}s} =\n"
    newString += f"= {self.author:^{box_length}s} =\n"
    
    # add dots around text
    newString += dotline
    
    # read in each line with a fixed length and border
    for i, line in enumerate(self.text.splitlines()):
      if i != 0:
         newString = newString + f"= {line:<{box_length}s} =\n"
      
    # add dots and border to the end
    newString += dotline
    newString += borders
    
    # return formatted string
    return newString
  def interact(self, player):
    pause(message = "You reach for the book...")
    clear()
    print(self)
    pause()
    pause("You put the book down.")
    
class Bookshelf(Feature):
  def __init__(self, *books, desc = story.interactions["bookshelfDEF"]):
    super().__init__(name="bookshelf")
    self.books = books
    self.desc = desc
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
      usr_input = input(">> ")
      if (usr_input != "n"):
        choice = int(usr_input) - 1
      else:
        choice = -1
    else:
      print(f"You reach for a book called \"{self.books[choice].title}\"")
      pause()
    if choice == -1:
      pass
    else:
      self.books[choice].interact(player)

class MagicMirror(Feature):
  def __init__(self):
    super().__init__(name="mirror")
    self.count = 0
  def interact(self, player):
    # when the user interacts with it the first time, they see a wink
    # the second time, they're drawn in by a mysterious force?
    if self.count == 1:
      print("Something pulls you into the mirror")
      player.victory = True
      pause(end=True)
    else:
      print("the mirror winks at you")
      self.count += 1
      pause()
  
class DeskWithScrewdiver(ItemFeature):
  def __init__(self, name="desk"):
    super().__init__(name, items.Screwdriver())
  def interact(self, player, room):
    pause("You find a screwdriver in the drawer.")
    room.items.append(self.items[0])
    # prompt("There is nothing of importance in the desk.")