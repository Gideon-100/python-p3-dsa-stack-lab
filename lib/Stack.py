class Stack:
    def __init__(self, items=None, limit=None):
        if items is None:
            self.items = []
        else:
            self.items = list(items)

        self.limit = limit  

    def isEmpty(self):
        return len(self.items) == 0

    def full(self):
        """Return True if stack is full (limit reached)."""
        if self.limit is None:
            return False
        return len(self.items) >= self.limit

    def push(self, item):
        if self.limit is not None and len(self.items) >= self.limit:
            return None   
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            return None
        return self.items.pop()

    def peek(self):
        if self.isEmpty():
            raise IndexError("peek from empty stack")
        return self.items[-1]

    def size(self):
        return len(self.items)

    def search(self, target):
        """
        Return how many elements are above the target in the stack.
        If not found, return -1.
        """
        if target in self.items:
            return len(self.items) - self.items.index(target) - 1
        return -1



