class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        v = self.stack[-1]
        return v


    def getMin(self) -> int:
        m = min(self.stack)
        return m
        
