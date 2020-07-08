class Feature:
  def __init__(self):
    super().__init__()
  def interact(self):
    raise NotImplementedError()

class Book(Feature):
  def __init__(self, title, text):
    self.title = title
    self.text = text
    
class Bookshelf(Feature):
  def __init__(self, *books):
    super().__init__()
    self.books = books
  def interact(self):
    # need to be able to see the bookshelf and interact ->
    # interaction should display the available books and an input
    # input should select which book to read <- EASTER EGGS?
    raise NotImplementedError()

class MagicMirror(Feature):
  def __init__(self):
    super().__init__()
    self.count = 0
  def interact(self):
    # when the user interacts with it the first time, they see a wink
    # the second time, they're drawn in by a mysterious force?
    self.count += 1
    

aliceInWonderland = Book("Alice in Wonderland", """Alice asked the Cheshire Cat, who was sitting in a tree, "What road do I take?"
                         The cat asked, "Where do you want to go?"
                         "I don’t know," Alice answered.
                         "Then," said the cat, "it really doesn’t matter, does it?" """)