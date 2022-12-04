# python3

from collections import deque

def max_sliding_window_deque(input_sequence, window_size):

    res = []

    # this queue stores the index, 
    # and the corresponding value of index is in a descending order
    max_queue = deque(maxlen=len(input_sequence))

    for i, val in enumerate(input_sequence):
        # if the index is out of the window,
        # pop out the index
        while max_queue and (max_queue[0] < i-window_size+1):
            max_queue.popleft()

        # if the value of index in the max_queue is smaller than the new input
        # pop out the index to maintain a descending order
        while max_queue and (input_sequence[max_queue[-1]] < val):
            max_queue.pop()

        max_queue.append(i)
        if i >= window_size - 1:
            res.append(input_sequence[max_queue[0]])

    return res


if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window_deque(input_sequence, window_size))


