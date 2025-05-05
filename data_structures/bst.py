class BSTNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def get_min(self):
        it = self
        while it.left is not None:
            it = it.left

        return it.val

    def get_max(self):
        it = self
        while it.right is not None:
            it = it.right

        return it.val
    
    def delete(self, val):
        if not self:
            return None
        
        if val < self.val:
            if self.left:
                self.left = self.left.delete(val)
                return self
        
        if val > self.val:
            if self.right:
                self.right = self.right.delete(val)
                return self
            
        if val == self.val:
            if not self.right:
                return self.left
            
            if not self.left:
                return self.right
            
            # self has both left and right nodes
            successor = self.right.get_min()
            self.val = successor
            self.right = self.right.delete(successor)

            return self

    def insert(self, val):
        if self.val is None:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
            else:
                self.left = BSTNode(val)

        elif val > self.val:
            if self.right:
                self.right.insert(val)
            else:
                self.right = BSTNode(val)
        
    def search(self, val):
        if val == self.val:
            return self
        
        if val < self.val:
            if self.left:
                return self.left.search(val)
            
        if val > self.val:
            if self.right:
                return self.right.search(val)

        return None
    
    def height(self):
        if not self.val:
            return 0
            
        left_h = 0
        right_h = 0
        
        if self.left:
            left_h = self.left.height()
            
        if self.right:
            right_h = self.right.height()

        return max([left_h, right_h]) + 1
