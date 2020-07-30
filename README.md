# Text Adventure

A text adventure game that is yet unnamed and will hopefully become a huge project.

## V2.3 Refactor

This version is focusing on new forms of user interaction to make gameplay more dynamic and enjoyable. Recent feature implementations make these new additions seem much easier.

### Under Development

* [x] Implement lock and key system
* [ ] Implement item combinations

### Future Release

Current implementation searches through all of player's keys and if any of them are a match for the door, the door is unlocked. I'd like to make players select which key to try.

#### Plan of Attack

For item combinations, I'm considering storing the data similary to how the world loads, in a dictionary with a touple as the key. The touple should contain the two items that can be combined, and the dict value should be a reference for the new item.

For the locked room, I'll need to create a new room type that defaults to locked. In order to unlock, it, you will need the correct item (probably going to be a new item base class called Key). The key implementation is probably going to be difficult but will be rewarding in the end. Each key will have a unique identifier, as will all locked rooms.

A new action will need to be created to unlock doors. The action should take the key and the room as a parameter, compare the unique IDs of both, and, if they match, change the state of the room to unlocked. This implementation will need to be built across multiple files, but should load easily from the story-based JSON file, as with all other things.

## V2.2 Refactor

In this release, I'll attempt to adjust tile creation to allow items and features to be auto-loaded from the JSON - with the intention of making the app more scalable and easier to maintain. Current setup is enough to begin creating new story elements.

### New This Version

* [x] Rooms load features and items from JSON
* [x] Implement new room class that can increment its own description and intro

## V2.1 Refactor

This version is primarily focused on restructuring files for ease of comprehension. Focus is on code readability and compartmentalization of data.

### Finished This Release

* Converted data files to JSON
* Altered file structure for better readability
* Altered printing function to allow for optional alignment flag in first character

## V2 Refactor

This refactor includes a variety of updates to the class system that will allow for more flexibility and scalability, as well as more interesting interactions for the user.

### Still Under Development

* [ ] Expand story - only tutorial is implemented
* [x] Refactor the way that stories are stored
