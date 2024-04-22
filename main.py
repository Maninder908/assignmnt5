class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.stack:
            return None
        return self.stack.pop()

    def __repr__(self):
        return f"<Stack ({len(self.stack)} element{'s' if len(self.stack) != 1 else ''}): [{', '.join(reversed(self.stack))}]>"
#Example usage
mystack = Stack()
mystack.push('A')
#print(mystack)  # Output: <Stack (1 element): [A]>

mystack.push('B')
mystack.push('C')
#print(mystack)  # Output: <Stack (3 elements): [C, B, A]>

#print(mystack.pop())  # Output: C
#print(mystack)  # Output: <Stack (2 elements): [B, A]>

#print(mystack.pop())  # Output: B
#print(mystack.pop())  # Output: A
#print(mystack.pop())  # Output: None