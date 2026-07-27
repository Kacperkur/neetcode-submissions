class MinStack:

    def __init__(self):
        self.items = []
        self.minStack = []

    def push(self, val: int) -> None:
        # append the value to the stack
        self.items.append(val)
        # if stack is empty
        if not self.minStack:
            self.minStack.append(val)
        # if the value is less than the last item in the minstack, append it to the min
        elif val < self.minStack[-1]:
            self.minStack.append(val)
        # if the stack is not empty and the value is >= than the last element of the minStack copy over the elements last known min
        else:
            self.minStack.append(self.minStack[-1])
        

    def pop(self) -> None:
        # pop both stacks
        self.items.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.items[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
        
