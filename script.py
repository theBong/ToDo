from items import *

a = Item(note = "a", done = True)
b = Item(note = "b", done = False)
b.updatedone(False)
print(b.done)


todd = Todo("Todd", [a,b])
print (todd.items[1].note)

print (str(todd))