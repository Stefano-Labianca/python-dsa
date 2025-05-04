class Node:
    def __init__(self, val):
        self.val = val
        self.next: Node | None = None

    def set_next(self, node):
        self.next = node

    def __repr__(self):
        return self.val


class LinkedList:
    def __init__(self):
        self.head: Node | None = None
        self.tail: Node | None = None
        self.size = 0

    def add_to_head(self, node: Node):
        if self.head is None:
            self.tail = node
        
        node.set_next(self.head)
        self.head = node
        self.size += 1

    def add_to_tail(self, node: Node):
        if (self.head is None) and (self.tail is None):
            self.head = node
            self.tail = node

            return
        
        if self.tail is None: return

        self.tail.set_next(node) 
        self.tail = node
        self.size += 1

    def remove_from_head(self):
        if self.head is None: 
            return None

        old_head = self.head
        self.head = self.head.next

        if self.head is None:
            self.tail = None
            old_head.next = None

        self.size -= 1
        return old_head

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.val)
        return " -> ".join(nodes)
