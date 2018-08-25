from items import *
from peewee import *
db = SqliteDatabase('todo.db')

lis_of_items = {}
lis_of_todo = {}


class Entry(Model):
	note = CharField(max_length = 100, unique = True)
	done = IntegerField(default = 0)

	class Meta:
		database = db

def save2db():
	for item in lis_of_items:
		try:
			Entry.create(note = lis_of_items[item].note,
								done = lis_of_items[item].done)
		except IntegrityError:
			entry = Entry.get(note = lis_of_items[item].note)
			entry.done = int(lis_of_items[item].done)
			entry.save()



def create_item():
	note = input("What is the note? \n")
	done = bool(input("Done status? \n"))
	id = input("Enter an item ID\n")

	item = Item(note=note, done=done)
	lis_of_items.update({ id : item })

	return "Created item with ID {}\n".format(str(id))


def create_todo():
	name = input("Name the ToDo!\n").title()
	items_ids = input("Type out IDs in a line separated by commas, no spaces \n").split(',')
	id = input("Enter a Dictionary ID \n")
	thing_list = []

	for id in items_ids:
		thing_list.append(lis_of_items[id])

	todo = Todo(name=name, things=thing_list)
	lis_of_todo.update({ id : todo})

	return "Created with ID {} \n".format(str(id))



db.connect()
db.create_tables([Entry], safe = True)

while(True):
	menu = ('1. Create an Item\n2. Create a ToDo\n3. save\nOther. Display list of' \
		    'items and ToDos\n\n')
	inp = int(input(menu))

	if inp == 1:
		print("")
		print(create_item())
	elif inp == 2:
		print("")
		print(create_todo())

	elif inp == 3:
		print("")
		print(save2db())
	else:
		print("\nList of Items: ")
		for key, value in lis_of_items.items():
			print("{}> {}".format(key, value))
		print("\nList of TodoLists")
		for key, value in lis_of_todo.items():
			print("{} = {} ".format(key, value))
		print("")
