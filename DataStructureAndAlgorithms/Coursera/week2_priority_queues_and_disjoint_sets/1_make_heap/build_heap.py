# python3

import math
#%%
class Heap():
    def __init__(self, n, data) -> None:
        self.size = n
        self.data = data
        self.swap_log = []

    @staticmethod
    def parent(i):
        return math.floor((i-1) / 2)

    @staticmethod
    def left_child(i):
        return 2 * i + 1

    @staticmethod
    def right_child(i):
        return 2 * i + 2

    def sift_down(self, i):
        min_index = i

        l = self.left_child(i)
        r = self.right_child(i)

        if l < self.size and self.data[l] < self.data[min_index]:
            min_index = l
        
        if r < self.size and self.data[r] < self.data[min_index]:
            min_index = r

        if i != min_index:
            self.data[i], self.data[min_index] = self.data[min_index], self.data[i]
            self.swap_log.append((i, min_index))
            self.sift_down(min_index)

    def build_heap(self):
        for i in range(self.size // 2, -1, -1):
            self.sift_down(i)
        return self.data


def main():
    # n = int(input())
    # data = list(map(int, input().split()))
    from numpy.random import default_rng

    rng = default_rng()
    numbers = rng.choice(20, size=10, replace=False)

    # assert len(data) == n

    data = [3,2,1,4,5,7,8,6,9,12]
    import heapq
    print(list(heapq.heapify(data)))

    heap = Heap(len(data), data)
    res = heap.build_heap()
    print(res)
    swaps = heap.swap_log
    
    # print(len(swaps))
    # for i, j in swaps:
    #     print(i, j)


if __name__ == "__main__":
    main()


# %%
