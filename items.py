class Item():
	def __init__(self, note = None, done = None, *args, **kwargs):
		
		if not (note or done):
			raise ValueError("One or more arguments are missing")

		self.note = note
		self.done = done

	def updatenote(self, note):
		self.note = str(note)
		return "To-DO has been updated to: " + self.note

	def updatedone(self, done):
		self.done = done
		return "Status has been updated to: " + str(self.done)


	def __str__(self):
		return self.note + " : " + str(self.done)




class Todo():
	items = []
	def __init__(self, name = None, things = None):
		if not (name or things):
			raise ValueError("One or more arguments are missing")
		
		self.name = name
		self.items.extend(things)

	def __len__(self):
		return len(self.items)

	def __iter__(self):
		yield from self.items

	def __str__(self):
		res = self.name + "> "

		for item in self.items:
			res += (str(item) + ", ")

		return res[:len(res)-2]

	def itemAtIndex(self, index):

		if index>len(self):
			raise ValueError("Exceeds maximum index")
		return self.items[index]

	def addItems(self, itemlist):
		if not isinstance(itemlist,list):
			raise TypeError("Please pass a list of items.")

		self.items.extend(itemlist)