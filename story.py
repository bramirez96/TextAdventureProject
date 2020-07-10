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
laundry on the floor. There's a bookshelf by the door.

You welcome the darkness.

Somewhere nearby, you can hear a faint but steady tapping.
You live alone. You listen harder and the tapping ceases.

There is a door to the north that leads to your living room.
""",
  "AptLR": """\
You're standing in your living room. You hear the
strange tapping sound again, louder than in your room. 
Is it coming from inside your apartment?

There is another bookshelf against the wall. You feel
a strange sense of guilt that you haven't read a book
for years. Like you've failed yourself somehow.

To the south is the bedroom.

To the west is your kitchen. When was the last time
you ate? The days are starting to blur together.

To the east is your bathroom. You don't have to go.
""",
  "AptKit": """\
You look around. The sink is full of dishes. How long
has it been since you've cleaned up? There's no way to
know for sure. 

You pause to listen as the tapping starts again. It sounds
more distant than it did in the living room.

Am I going crazy?

To the east is your living room. There are no other doors.
""",
  "AptBath1": """\
You look around. It's a fairly standard bathroom with
a mirror above the sink, a toilet, and a shower.

You stop and listen as you hear the tapping again,
this time louder than ever. You know it's nearby. 
You can't shake the eerie feeling that you're in a
fishtank, and someone is tapping against your glass.

What on Earth is that sound?? All at once it stops.

To the west is your living room.
""",
  "AptBath2": """\
Standing in the bathroom, you ponder what you saw in the mirror.

It's not possible to see your reflection blink, right? Some part of
you wants to look again but the fear you feel is almost tangible.

As you sit, attempting to rationalize what you've just seen,
the tapping begins again - slowly at first, but building rapidly,
until it becomes a ferocious pounding.

Your heart races as you contemplate your next move.

To the west is your living room, although you're not very
interested in what's going on in there...
"""
}
interactions = {
  "mirror1": """...and stare into your reflection. It's almost difficult
to recognize yourself. Where have all of the years gone?

That all-too familiar dread creeps in that life is
somehow rushing past you, and you just can't keep up,
no matter how hard you try.

As you ponder the brevity of life, your thoughts are
stopped dead in their tracks...

Did your reflection just blink???

Frantic, you turn away.
""",
  "mirror2": """...slowly, as if you're afraid of your reflection.

Your reflection that isn't your reflection. There's a
fire in her eyes as she pounds at the mirror with both
fists. Are you finally losing it?

"WHAT DO YOU WANT FROM ME?" you scream.

She stops. Slowly, as if she has a secret that you were
never destined to know, her lips turn up into a cruel,
inhuman smile. Raising her hand, she beckons you near.

"What are you?" the panic in your voice is tangible.

Her smile softens. Cocking her head as if examing you
closer, she laughs as she turns and runs.

"This can't be happening. It's not real." Slowly raising
your hand, you approach the mirror, determined that the
events of the past few minutes were a delusion.

You want to believe your lie, but as you reach out to touch
the mirror in front of you - the mirror that isn't a mirror,
the mirror with no reflection - you feel the familiar panic
welling up deep in your throat.

The second your fingers touch the glass, you begin to fall.
""",
  "falling": """\
Engulfed in a darkness thicker than any you've experienced,
you trash about, desperately searching for any light, anything
to tell you where you are or what's happening.

You see nothing.

As you continue falling, seemingly forever, you try to assure
yourself that this is just a dream. A psychotic break. Anything
other than reality. What a comfort it would be to know that it
was merely your perception that had changed, and that reality
remained safely intact outside of your illness-stricken mind.

But as the last trace of comfort vanishes from your thoughts,
you begin to hear music. 

Below you? Above you? No way to know. Direction, space, time,
it's all meaningless now.

Tears well up in your eyes as you accept that you will never
stop falling. Clutching your legs up to your chest, you drift
off to sleep as you fall deeper into oblivion.
""",
  "bookshelfDEF": "You see a bookshelf.\n\nWhich book would you like to read?",
  "bsAPTLR": """In front of you is your trusty bookshelf.
Titles that you once loved lay covered
in dust, forgotten.

Which book would you like to read?
""",
  "bsAPTBR": """Although it's a bookshelf, it contains
mostly CDs, DVDs, and memorabilia.

You manage to find one book on the bottom shelf.
"""
}
items = {
  "aptKitGum": """Next to a stack of unopened mail on the kitchen table,
you see a piece of gum.
"""
}