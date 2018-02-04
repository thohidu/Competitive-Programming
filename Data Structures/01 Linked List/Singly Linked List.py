# Node class
class Node:
    # Constructor
    def __init__(self):
        self.data = None
        self.next = None

    # Set the data in the Node
    def set_data(self, data):
        self.data = data

    # Return the data of the Node
    def get_data(self):
        return self.data

    # Set the next value of the Node
    def set_next(self, next):
        self.next = next

    # Return the next value of the Node
    def get_next(self):
        return self.next

    # Check if the Node has the next value
    def has_next(self):
        return self.next is not None


# Singly LinkedList class
class SinglyLinkedList:
    # Constructor
    def __init__(self):
        self.head = None

    # Insert a new node in the LinkedList
    def list_insert(self, position, data):
        length_of_list = self.list_length()
        if position > length_of_list or position < 0:
            return None
        elif position == 0:
            self.insert_at_start(data)
        elif position == length_of_list:
            self.insert_at_end(data)
        else:
            new_node = Node()
            new_node.set_data(data)
            current = self.head
            count = 0

            while count < position - 1:
                current = current.get_next()
                count += 1

            new_node.set_next(current.get_next())
            current.set_next(new_node)

    # Insert a new node at the start of LinkedList
    def insert_at_start(self, data):
        new_node = Node()
        new_node.set_data(data)

        if self.list_length() == 0:
            self.head = new_node
        else:
            new_node.set_next(self.head)
            self.head = new_node

    # Insert a new node at the start of LinkedList
    def insert_at_end(self, data):
        new_node = Node()
        new_node.set_data(data)
        current = self.head

        while current is not None:
            current = current.get_next()

        current.set_next(new_node)

    # Return the length of the LinkedList
    def list_length(self):
        current = self.head
        count = 0

        while current is not None:
            count += 1
            current = current.get_next()

        return count


LinkedList = SinglyLinkedList()