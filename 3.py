class StackBasedQueue():
    def __init__(self):
        self._size = 0
        self._InboundStack = []
        self._OutboundStack = []

    def __repr__(self):
        plural = '' if self._size == 1 else 's'
        values = [str(c) for c in self._InboundStack]
        values.extend([str(c) for c in self._OutboundStack][::-1])
        return f'<StackBasedQueue ({self._size} element{plural}): [{", ".join(values)}]>'

    def enqueue(self, data):
        self._InboundStack.append(data)
        self._size += 1

    def dequeue(self):
        if not self._OutboundStack:
            # Transfer elements from Inbound stack to Outbound stack
            while self._InboundStack:
                self._OutboundStack.append(self._InboundStack.pop())
        if not self._OutboundStack:
            # If both stacks are empty, raise an error
            raise IndexError("Queue is empty")
        self._size -= 1
        return self._OutboundStack.pop()
