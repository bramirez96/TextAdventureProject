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
You live alone. You listen harder and the tapping ceases.\
""",
  "AptLR": """\
You're standing in your living room. Last night's dinner sits
on the coffee table, unfinished. You hear the strange tapping
sound again, slightly louder than when you woke.

Is it coming from inside your apartment?\
""",
  "AptKit": """\
You look around. The sink is full of dishes. How long
has it been since you've cleaned up? There's no way to
know for sure. 

You pause to listen as the tapping starts again. It sounds
more distant than it did in the living room.

Maybe you're just hearing things...\
""",
  "AptBath1": """\
You look around. It's a fairly standard bathroom with a
sink, toilet, and a shower. The trashcan is overflowing, 
and the hamper in the corner is nearly there as well.

You stop and listen as you hear the tapping again, this
time louder than ever. You know it's nearby. You can't
shake the eerie feeling that you're in a fishtank, and
someone is tapping against your glass.

What on Earth is that sound?? All at once it stops.\
""",
  "AptBath2": """\
Standing in the bathroom, you ponder what you saw in the mirror.

It's impossible to see your reflection blink, right? Some part of
you wants to look again but the fear you feel is almost tangible.

As you sit, attempting to rationalize what you've just seen,
the tapping begins again - slowly at first, but building rapidly,
until it becomes a ferocious pounding.

Your heart races as you contemplate your next move.\
""",
  "AptBath3": """\
Momentarily frozen in shock, you consider what just happened.

Where your apartment once felt safe, you now feel as though you
are under attack by something dark and sinister. Reflections
don't just run away... they can't! Right?

Thinking back a few years, you try and remember what those old
hallucinations felt like. They felt real enough at the time, but
they never looked like this. This was new.

Your heart races as you contemplate your next move.\
"""
}
interactions = {
  "mirror1": """\
...and stare into your reflection. It's almost difficult
to recognize yourself. Where have all of the years gone?

That all-too familiar dread creeps in that life is
somehow rushing past you, and you just can't keep up,
no matter how hard you try.

As you ponder the brevity of life, your thoughts are
stopped dead in their tracks...

Did your reflection just blink???

Frantic, you turn away.\
""",
  "mirror2": """\
...slowly, as if you're afraid of your reflection.

Your reflection that isn't your reflection. There's a
fire in her eyes as she pounds at the mirror with both
fists. Are you finally losing it?

"WHAT DO YOU WANT FROM ME?" you scream.

She stops. Slowly, as if she has a secret that you were
never destined to know, her lips turn up into a cruel,
inhuman smile. Raising her hand, she beckons you near.

"What are you?" you ask, barely managing a whisper.

Her smile softens. Cocking her head as if examining you
closer, she laughs as she turns and runs.\
""",
  "mirror3": """\
Everything in your bathroom can be seen reflected in the
terrifying glass except your reflection. Where did she go?

"This can't be happening. It's not real." Slowly raising
your hand, you approach the mirror, determined that the
events of the past few minutes were a paranoid delusion.

Pausing momentarily, you reassure yourself that since what
you were seeing was impossible, it couldn't be happening.

Trying in vain to believe the comforting lie, you reach out
to touch the mirror in front of you - the mirror that isn't
a mirror, the mirror with no reflection - as you feel that
familiar panic welling up deep in your throat.

The second your fingers touch the glass, you begin to fall.\
""",
  "falling": """\
Engulfed in a darkness thicker than any you've experienced, you
trash about, desperately searching for any light, anything to tell
you where you are or what's happening.

You see nothing.

As you fall deeper and deeper, seemingly forever, you try to assure
yourself that this is just a dream. A psychotic break. Anything
other than reality. What a comfort it would be to know that it was
merely your perception that had changed, and that reality remained
safely intact outside of your illness-stricken mind.

As the last trace of comfort vanishes from your thoughts, and your
final shred of hope slips away, you begin to hear music. 

Below you? Above you? No way to know. Direction, space, time...

It's all meaningless now.

Tears well up in your eyes as you accept that you will never stop
falling. Clutching your legs up to your chest, you drift off to
sleep as you fall endlessly into oblivion.\
""",
  "bookshelfDEF": "You see a bookshelf.\n\nWhich book would you like to read?",
  "bsAPTLR": """\
In front of you is your trusty bookshelf. Amidst the stacks
of papers and carefully curated bric-a-brac, titles that
you once loved lay covered in dust, forgotten.

Which book would you like to read?\
""",
  "bsAPTBR": """\
Although it's a bookshelf, it contains mostly CDs,
DVDs, and memorabilia. Delicately, you reposition a
figurine that was slightly out of place.

You manage to find one book on the bottom shelf.
""",
  "bookDEF": "You see a book.",
  "mirrorIntro1": "On the wall above the sink is a large, ornate mirror.",
  "mirrorIntro2": "On the wall above the sink is a large, ornate mirror. Thinking\n\
about it fills you with a deep dread.",
  "mirrorIntro3": """\
The mirror is still on the wall, but you have no reflection.\
"""
}

items = {
  "aptKitGum": """\
Next to a stack of unopened mail on the kitchen table,
you see a piece of gum.\
"""
}

featureIntros = {
  "aptLRBookshelf": """\
There is another bookshelf against the wall. You feel
a strange sense of guilt that you haven't read a book
for years. Like you've failed yourself somehow.\
""",
"aptBRBookshelf": """\
By the door is a bookshelf. Are there any books on it?\
"""
}
