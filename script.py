from items import *

a = Item(note = "a", done = True)
b = Item(note = "b", done = False)
c = Item(note = "c", done = False)
b.updatedone(False)
print(b.done)


todd = Todo("Todd", [a,b])

print (todd.items[1].note)

print (str(todd))

todd.addItems([c])

print (str(todd))

print (todd.items[2].note)

todd.delItem(c)

print (str(todd))