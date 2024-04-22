class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.items:
            return None
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

def check_balance(text):
    stack = Stack()
    opening_brackets = ['(', '[', '{']
    closing_brackets = [')', ']', '}']
    bracket_pairs = {'(': ')', '[': ']', '{': '}'}
    count = 0

    for i, char in enumerate(text):
        if char in opening_brackets:
            stack.push(char)
        elif char in closing_brackets:
            if stack.is_empty():
                return f"Match error at position {i}"
            top_bracket = stack.pop()
            if bracket_pairs[top_bracket] != char:
                return f"Match error at position {i}"
            else:
                count += 1

                if stack.is_empty():
                    return f"Ok - {count}"
                else:
                    return f"Match error at position {len(text) - len(stack.items)}"
            # Example usage

            # print(check_balance("a(b)c(([d][e{f}])g)("))  # Output: Match error at position 19
            # print(check_balance("a(b)c([d][e{f}])g)"))    # Output: Match error at position 16
            # print(check_balance("a(b)c([d][e{f}])g"))     # Output: Ok - 3