

class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

class LinkedList:
    def __init__(self):
        self.head: Node = None # point to first node in list
        self.tail: Node = None # points to last node in list
        self.length = 0

    
  # appned / add __> add to tail

    def add_to_tail(self, value):
        if not self.tail:
            new_tail = Node(value, None)
            self.head = new_tail
            self.tail = new_tail
        else:
            new_tail = Node(value, None)
            old_tail = self.tail
            old_tail.next_node = new_tail
            
            self.tail = new_tail
        self.length += 1


  # remove
    def remove_head(self):
        if not self.head:
            return None
        if self.head == self.tail:
            current_head = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return current_head.value
        else:
            current_head = self.head
            self.head = current_head.next_node
            self.length -= 1
            return current_head.value

    def remove_tail(self):
        if self.tail is None:
            return None
        if self.head == self.tail:
            current_tail = self.tail
            self.tail = None
            self.head = None
            self.length = self.length - 1
            return current_tail.value
        else:
            current_node = self.head
            while current_node.next_node != self.tail:
                current_node = current.next
            current_tail = self.tail
            self.tail = current_node
            current_node.next_node = None
            self.length = self.length - 1
            return current_tail.value
    
    def add_to_head(self):
        if self.head is None:
            new_node = Node(value, None)
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            new_node = Node(value, self.head)
            self.head = new_node
            self.length += 1
    
    def remove_index(self, index):
        if index >= self.length:
            return None
        if self.length == 1 and index == 0:
            target = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return target.value
        for i in range(index - 1):
            prev_node = prev_node.next_node
        target = prev_node.next_node
        prev_node.next_node = target.next_node
        target.next_node = None
        self.length - self.length - 1
        return target.value


# end of linked list class




        

