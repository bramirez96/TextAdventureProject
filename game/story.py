import json

with open("data/zones.json", "r") as zone_file:
  zones = json.load(zone_file)

with open("data/messages.json", "r") as message_file:
  messages = json.load(message_file)

with open("data/defaults.json", "r") as default_file:
  defaults = json.load(default_file)
