import os

def pause(message = "Press enter to continue...\n", end =False):
  if end:
    input("To be continued...")
  else:
    input(message)

def borderpr(string):
    # initialize helpful variables for printing
    box_length = 0
    dots = "..."
    blanks = ""
    borders = ""
    
    # get max line length in specific text
    for line in string.splitlines():
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
    
    # add dots around text
    newString += dotline
    
    # read in each line with a fixed length and border
    for i, line in enumerate(string.splitlines()):
      newString = newString + f"= {line:<{box_length}s} =\n"
      
    # add dots and border to the end
    newString += dotline
    newString += borders
    
    # return formatted string
    print(newString)

def prompt(string = "What do you do?"):
  print(string)
  x = input(">> ")
  return x.lower()

def clear():
   os.system("cls")
