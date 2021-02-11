'''
# https://www.youtube.com/watch?v=JlMyYuY1aXU&ab_channel=BrianFaure

Linked lists are not a built in feature of python language. A way to store data in an ordered matter. Comparable to arrays (an array is a fixed size chunk of memory).

LL has no strict ordering in memory. Ordering is controlled by the data structure. 

'''

class Node:
    def __init__(self, data = None):
        self.data = data 
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
        current_node.next = new_node

    def length(self):
        current_node = self.head
        total_nodes = 0
        while current_node.next != None:
            total_nodes += 1
            current_node = current_node.next
        return total_nodes 

    def display(self):
        elements = []
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
            elements.append(current_node.data)
        print(elements)

    def get(self, index):
        if index >= self.length():
            print('ERROR: "get" index out of range')
            return None
        current_index = 0
        current_node = self.head
        while True:
            current_node = current_node.next
            if current_index == index:
                return current_node.data
            current_index += 1

    def erase(self, index):
        if index >= self.length():
            print('ERROR: "get" index out of range')
            return 
        current_index = 0
        current_node = self.head
        while True:
            last_node = current_node
            current_node = current_node.next
            if current_index == index:
                last_node.next = current_node.next
                return
            current_index += 1

my_list = LinkedList()

my_list.display()
my_list.append(0)
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.display()
print(my_list.get(1))
my_list.display()
my_list.erase(1)
my_list.display()