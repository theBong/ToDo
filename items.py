class Item():
    def __init__(self, note=None, done=None, *args, **kwargs):
        if not (note or done):
            raise ValueError("One or more arguments are missing")

        if not isinstance(done, bool):
            raise TypeError("Boolean argument expected for done")

        self.note = note
        self.done = done

    def update_note(self, note):
        self.note = str(note)
        return "To-DO has been updated to: {}".format(self.note)

    def updatedone(self, done):
        self.done = done
        return "Status has been updated to: {}".format(str(self.done))

    def __str__(self):
        return "{}:{}".format(self.note, self.done)


class Todo():
    items = []
    def __init__(self, name=None, things=None):
        if not (name or things):
            raise ValueError("One or more arguments are missing")

        self.name = name
        self.items.extend(things)

    def __len__(self):
        return len(self.items)

    def __iter__(self):
        yield from self.items

    def __str__(self):
        res = "{}> ".format(self.name)

        for item in self.items:
            res += "{}, ".format(str(item))

        return res[:len(res)-2]

    def item_at_index(self, index):
        if index > len(self):
            raise ValueError("Exceeds maximum index")
        return self.items[index]

    def add_items(self, item_list):
        if not isinstance(item_list, list):
            raise TypeError("Please pass a list of items.")
        self.items.extend(item_list)

    def del_item(self, item):
        if item in self.items:
            del self.items[self.items.index(item)]
        else:
            raise ValueError("No such value")
