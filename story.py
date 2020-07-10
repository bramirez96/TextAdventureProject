intro = [
  """     Text Adventure Game
       Brandon Ramirez

          Controls
go   -> move in a direction
get  -> pick up an item
look -> interact with objects
i    -> view your inventory
help -> view controls
""",
]
roomIntro = {
  "AptBed": """\
You wake up to a loud blaring sound, just like any 
other day. Reaching over, you turn off your alarm,
and are plunged into a comforting silence.

Rubbing the sleep from your eyes, you look around
the dark room before you. The curtains on the window
are drawn tight, preventing any sunlight from entering.
In one corner you can just about make out a pile of
laundry on the floor.

You welcome the darkness.

Somewhere nearby, you can hear a faint but steady tapping.
You live alone. You listen harder and the tapping ceases.

There is a door to the north that leads to your living room.
""",
  "AptLR": """\
You're standing in your living room. You hear the
strange tapping again, louder this time. 
Is it coming from inside your apartment?

There is a bookshelf against the wall. You feel a
strange sense of guilt that you haven't read a book
for years. Like you've failed yourself somehow.

To the south is the bedroom you just came from.

To the west is your kitchen. When was the last time
you ate? The days are starting to blur together.

To the east is your bathroom. You don't need to go.
""",
  "AptKit": """\
You look around. The sink is full of dishes. How long
has it been since you've cleaned up? There's no way to
know for sure. Next to a stack of unopened mail on
the kitchen table, you see a piece of gum.

You pause to listen as the tapping starts again. It sounds
more distant than it did in the living room.

Am I going crazy?

To the east is your living room. There are no other doors.
""",
  "AptBath": """\
You look around. It's a fairly standard bathroom with a
mirror above the sink, a toilet, and a shower.

You stop in your tracks as you hear the tapping again,
this time louder than ever. You know it's nearby. 
You can't shake the eerie feeling that you're in a
fishtank, and someone is tapping against your glass.

What on Earth is that sound??

To the west is your living room.
"""
}
interactions = {
  "mirror1": "",
  "bookshelfDEF": "You see a bookshelf.\n\nWhich book would you like to read?",
  "bookshelfApt": """You look at the bookshelf. Titles that you once
loved lay covered in dust, forgotten.

Which book would you like to read?
"""
}