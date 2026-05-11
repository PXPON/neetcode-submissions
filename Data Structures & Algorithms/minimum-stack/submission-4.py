# Something about an invariant
# minstack[-1] is always the minimum of every element in a stack

# The minimum value is the current value if minStack has nothing in it
# or the current value is less than the value already in it

class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        minVal = val if not self.minStack else min(val, self.minStack[-1])
        self.minStack.append(minVal)

    def pop(self) -> None:
        popped = self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
