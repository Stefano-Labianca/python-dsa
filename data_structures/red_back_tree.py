class RBNode:
    def __init__(self, val):
        self.red = False
        self.parent: RBNode | None = None
        self.val = val
        self.left: RBNode | None = None
        self.right: RBNode | None = None

class RBTree:
    def __init__(self):
        self.nil = RBNode(None)
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root: RBNode = self.nil

    def search(self, val):
        curr = self.root
        while curr is not None and curr != self.nil and val != curr.val:
            if val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        return curr
    
    def insert(self, val):
        new_node = RBNode(val)
        new_node.parent = None
        new_node.left = self.nil
        new_node.right = self.nil
        new_node.red = True

        parent = None
        current = self.root

        while current != self.nil and current is not None:
            parent = current
            if new_node.val == current.val:
                return
            
            if new_node.val < current.val:
                current = current.left
            elif new_node.val > current.val:
                current = current.right
            
        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif new_node.val < parent.val:
            parent.left = new_node
        else:
            parent.right = new_node

        self.__balance_insert(new_node)

    def __balance_insert(self, new_node):
        current = new_node
        while current != self.root and current.parent.red:
            parent = new_node.parent
            grandparent = parent.parent
            uncle = None
            
            if grandparent is not None:
                if grandparent.left == parent:
                    uncle = grandparent.right
                else:
                    uncle = grandparent.left

            if parent == grandparent.right:
                if uncle is not None and uncle.red:
                    parent.red = False
                    uncle.red = False
                    grandparent.red = True
                    current = grandparent
                elif uncle is not None and not uncle.red:
                    if current == parent.left:
                        current = parent
                        self.__rotate_right(current)
                        parent = current.parent
                    parent.red = False
                    grandparent.red = True
                    self.__rotate_left(grandparent)
            elif parent == grandparent.left:
                if uncle is not None and uncle.red:
                    uncle.red = False
                    parent.red = False
                    grandparent.red = True
                    current = grandparent
                elif uncle is not None and not uncle.red:
                    if current == parent.right:
                        current = parent
                        self.__rotate_left(current)
                        parent = current.parent
                    parent.red = False
                    grandparent.red = True
                    self.__rotate_right(grandparent)

        self.root.red = False     

    def __rotate_left(self, pivot_parent):
        if pivot_parent == self.nil or pivot_parent.right == self.nil:
            return
        
        pivot = pivot_parent.right
        pivot_parent.right = pivot.left
        if pivot.left != self.nil:
            pivot.left.parent = pivot_parent

        pivot.parent = pivot_parent.parent
        if pivot_parent.parent is None:
            self.root = pivot
        elif pivot_parent == pivot_parent.parent.left:
            pivot_parent.parent.left = pivot
        else:
            pivot_parent.parent.right = pivot
        pivot.left = pivot_parent
        pivot_parent.parent = pivot

    def __rotate_right(self, pivot_parent):
        if pivot_parent == self.nil or pivot_parent.left == self.nil:
            return
        pivot = pivot_parent.left
        pivot_parent.left = pivot.right
        if pivot.right != self.nil:
            pivot.right.parent = pivot_parent

        pivot.parent = pivot_parent.parent
        if pivot_parent.parent is None:
            self.root = pivot
        elif pivot_parent == pivot_parent.parent.right:
            pivot_parent.parent.right = pivot
        else:
            pivot_parent.parent.left = pivot
        pivot.right = pivot_parent
        pivot_parent.parent = pivot
