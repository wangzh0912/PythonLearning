#python3
import sys

from collections import deque

class Stack():
    def __init__(self):
        self._stack = deque()
        self._max_stack = deque()

    def push(self, val):
        self._stack.append(val)

        # if the input value is larger than the last value in the max_stack
        # push into the max_stack
        if not self._max_stack:
            self._max_stack.append(val)
        elif val >= self._max_stack[-1]:
            self._max_stack.append(val)

    def pop(self):
        assert(len(self._stack))
        val = self._stack.pop()

        # if the poped value equals to the last value in the max_stack
        # pop out the max_stack
        if self._max_stack and val == self._max_stack[-1]:
            self._max_stack.pop()

    def max(self):
        assert(len(self._max_stack))
        return self._max_stack[-1]


if __name__ == '__main__':

    stack = Stack()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == 'push':
            stack.push(int(query[1]))
        elif query[0] == 'pop':
            stack.pop()
        elif query[0] == 'max':
            print(stack.max())
        else:
            assert(0)
