# python3

import sys
import threading

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size

def compute_height(parents):
    depth = {-1: 0}
    while len(depth) <= len(parents):
        for child, parent in enumerate(parents):
            if parent in depth:
                depth[child] = depth[parent] + 1
    return max(depth.values())

def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(parents))

threading.Thread(target=main).start()
