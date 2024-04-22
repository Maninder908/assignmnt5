def get_pairs(numbers):
    even_queue = Queue()
    odd_queue = Queue()
    pairs = []

    for num in numbers:
        if num % 2 == 0:  # Even number
            if not odd_queue.is_empty():
                pairs.append((num, odd_queue.dequeue()))
            else:
                even_queue.enqueue(num)
        else:  # Odd number
            if not even_queue.is_empty():
                pairs.append((even_queue.dequeue(), num))
            else:
                odd_queue.enqueue(num)
    return pairs
