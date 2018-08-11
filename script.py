from items import *

lis_of_items = {}
lis_of_todo = {}

def createItem():
	inpNote = input("What is the note \n")
	inpDone = bool(input("Done status? \n"))
	inpID = input("Enter a Item ID\n")

	item = Item(note = inpNote, done = inpDone)

	lis_of_items.update({ inpID : item })
	return "Created item with ID " + str(inpID)

def createTodo():

	inpName = input("Name the ToDo!\n").title()
	inpItemsIDs = input("Type out IDs in a line separated by commas, no spaces \n").split(',')
	inpID = input("Enter a Dictionary ID \n")
	thinglist = []

	for ID in inpItemsIDs:
		thinglist.append(lis_of_items[ID])

	ToDo = Todo(name = inpName, things = thinglist)
	lis_of_todo.update({ inpID : ToDo})

	return "Created  with ID " + str(inpID)


while (True):
	
	inp = int(input('''
1: Create an Item
2: Create a ToDo
Other: Display list of items and ToDos
'''))

	if inp == 1:
		print("")
		print(createItem())

	elif inp == 2:
		print("")
		print(createTodo())

	else:
		print("")
		print("List of Items: ")
		for keys, values in lis_of_items.items():
			print(keys + "> " + str(values))
		print("")
		print("List of TodoLists")
		for keys, values in lis_of_todo.items():
			print(keys + " = " + str(values))


