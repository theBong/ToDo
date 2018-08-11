from items import *

lis_of_items = {}
lis_of_todo = {}

while (True):
	
	inp = menu()

	if inp == 1:

		print(createItem())

	elif inp == 2:

		createTodo()

	elif inp == 3:


def createItem():
	inpNote = ""
	inpDone = bool()
	inpID = ""

	item = Item(note = inpNote, done = inpDone)

	lis_of_items.update({ inpID : item })

	return "Created item number " + str(lis_of_items.index(item))

def createTodo():

	inpName
	inpItemsIDs
	inpID
	thinglist = []

	for ID in inpItemsIDs:
		thinglist.append(lis_of_items[ID])


	ToDo = Todo(name = inpName, things = thinglist )

	lis_of_todo.update({ inpID : ToDo})