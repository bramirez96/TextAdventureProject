class Feature:
  def __init__(self):
    super().__init__()
  def interact(self, player):
    player.interact(feature)
    
class Book(Feature):
  def __init__(self, title, text):
    self.title = title
    self.text = text
  def __str__(self):
    newString = f"=== {self.title} ===\n";
    for line in iter(self.text.splitlines()):
      newString = newString + f"=== {line}\n"
    return newString
  def interact(self, player):
    print(self)
    input("Press enter to continue...")
    
class Bookshelf(Feature):
  def __init__(self, *books):
    super().__init__()
    self.books = books
  def interact(self, player):
    # need to be able to see the bookshelf and interact ->
    # interaction should display the available books and an input
    # input should select which book to read <- EASTER EGGS?
    print("Which book do you want to read?")
    for i, book in enumerate(self.books):
      print(f"{i}: {book.title}")
    input(">> ")
    self.books[i].interact(player)

class MagicMirror(Feature):
  def __init__(self):
    super().__init__()
    self.count = 0
  def interact(self, player):
    # when the user interacts with it the first time, they see a wink
    # the second time, they're drawn in by a mysterious force?
    if self.count == 1:
      print("Something pulls you into the mirror")
      player.victory = True
    else:
      print("the mirror winks at you")
      self.count += 1
    

aliceInWonderland = Book("Alice in Wonderland", """Alice asked the Cheshire Cat, who was sitting in a tree, "What road do I take?"
The cat asked, "Where do you want to go?"
"I don’t know," Alice answered.
"Then," said the cat, "it really doesn’t matter, does it?"
""")