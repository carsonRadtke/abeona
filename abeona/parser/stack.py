class Stack:
    class StackNode:
        def __init__(self, data, bottom):
            self.data = data
            self.bottom = bottom

    def __init__(self):
        self.top = None

    def push(self, data):
        self.top = Stack.StackNode(data, self.top)

    def pop(self):
        ret = self.peek()
        self.top = self.top.bottom
        return ret

    def peek(self):
        return self.top.data
