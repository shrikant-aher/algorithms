
class Node(object):

    def __init__(self, data=None, nextNode=None):
        self.data = data
        self.nextNode = nextNode

    def __str__(self):
        return str(self.data)

    def get_data(self):
        return self.data

    def get_next(self):
        return self.nextNode

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, next_node):
        self.nextNode = next_node


class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_data = Node(data)
        new_data.set_next(self.head)
        self.head = new_data

    def size(self):
        current_node = self.head
        count = 0
        while current_node:
            count += 1
            current_node = current_node.get_next()
        return count

    def search(self, data):
        current_node = self.head
        found = False
        while current_node and found is False:
            if current_node.get_data() == data:
                found = True
            else:
                current_node = current_node.get_next()
        if not current_node:
            raise ValueError("data not found")
        return current_node

    def delete(self, data):
        current_node = self.head
        previous = None
        found = False
        while current_node and found is False:
            if current_node.get_data() == data:
                found = True
            else:
                previous = current_node
                current_node = current_node.get_next()
            if not current_node:
                raise ValueError("Element not in list")
            if not previous:
                self.head = current_node.get_next()
            else:
                previous.set_next(current_node.get_next())

    def find_middle(self):
        linkedlist_size = self.size()
        if linkedlist_size % 2 == 0:
            return linkedlist_size / 2
        else:
            return (linkedlist_size + 1) / 2

