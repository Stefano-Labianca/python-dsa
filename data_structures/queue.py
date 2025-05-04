from data_structures.linked_list import LinkedList, Node


class Queue:
    def __init__(self):
        self.list = LinkedList()

    def push(self, item):
        self.list.add_to_tail(Node(item))

    def pop(self):
        if self.is_empty():
            return None
        
        return self.list.remove_from_head()

    def peek(self):
        if self.is_empty():
            return None
        return self.list.tail

    def size(self):
        return self.list.size

    def is_empty(self) -> bool:
        return self.size() == 0
    
    def __iter__(self):
        node = self.list.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(str(node.val))
        return " <- ".join(nodes)