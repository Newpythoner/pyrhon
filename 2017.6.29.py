class Stack:
    def __init__(self,start = []):
        self.stack = []
        for x in start:
            self.push(x)

    def isEmpty (self):
        if self.stack == []:
            return True
        else:
            return False

    def push (self,obj):
        self.stack.append(obj)
        
    def pop(self):
        return self.stack.pop()

    def top (self):
        return self.stack[-1]

    def bottom (self):
        return self.stack[0]

