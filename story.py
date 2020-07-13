import json

with open("data/story.json", "r") as story_file:
  story = json.load(story_file)

messages,\
  defaults,\
  zones\
   = story.values()

# for zone in zones:
#   rooms = zones[zone]
#   for room in rooms:
#     # room is currently the key of the room obj
#     features = rooms[room]["features"]
#     items = rooms[room]["items"]
#     print(f"{room}: ->")
#     print(f"  feats-")
#     for feature in features:
#       print("    " + feature)
#     print(f"  items-")
#     for item in items:
#       print("    " + item)