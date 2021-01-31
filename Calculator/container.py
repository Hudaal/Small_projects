class Container:
    """Base"""
    def __init__(self):
        self. items = []

    def size(self):
        """Return number o f elements in self . i t ems"""
        return len(self.items)

    def is_empty(self):
        """is empty"""
        if len(self.items) == 0:
            return True
        else:
            return False

    def push(self, item):
        """for all"""
        self.items.append(item)

    def pop(self):
        """to override"""
        if self.is_empty():
            raise NotImplementedError
        return self.items.pop(0)

    def peek(self):
        """to override"""
        if self.is_empty():
            raise NotImplementedError
        return self.items[-1]


class Queue(Container):
    """override"""
    def __init__(self):
        super(Queue, self).__init__()

    def peek(self):
        """first ele"""
        if self.is_empty():
            return False
        return self.items[0]

    def pop(self):
        """first ele"""
        if self.is_empty():
            return False
        return self.items.pop(0)


class Stack(Container):
    """override"""
    def __init__(self):
        super(Stack, self).__init__()

    def peek(self):
        """last ele"""
        if self.is_empty():
            return False
        return self.items[-1]

    def pop(self):
        """last ele"""
        if self.is_empty():
            return False
        return self.items.pop(-1)


def main():
    stack = Stack()
    stack.push(2)
    stack.push(5)
    stack.push(1)
    stack.push(9)
    print(stack.peek())
    print(stack.items)

# main()
