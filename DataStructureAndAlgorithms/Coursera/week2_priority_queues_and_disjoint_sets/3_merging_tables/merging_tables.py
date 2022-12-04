# python3


class Database:

    def __init__(self, row_counts):
        self.row_counts = row_counts
        self.max_row_count = max(row_counts)
        n_tables = len(row_counts)
        self.ranks = [0] * n_tables
        self.parents = list(range(n_tables))

    def merge(self, dst, src):

        dst_parent = self.get_parent(dst)
        src_parent = self.get_parent(src)

        # if source and destination are already merged
        if src_parent == dst_parent:
            return False

        # else, merge two components
        if self.ranks[src_parent] >= self.ranks[dst_parent]:
            self.parents[src_parent] = dst_parent
        else:
            self.parents[dst_parent] = src_parent
            # if self.ranks[src_parent] == self.ranks[dst_parent]:
            #     self.ranks[src_parent] += 1
        
        # copy from source to destination
        self.row_counts[dst_parent] += self.row_counts[src_parent]
        # clear the source table
        self.row_counts[src_parent] = 0
        # calculate the max row counts
        self.max_row_count = max(self.max_row_count, self.row_counts[dst_parent])

        return True

    def get_parent(self, root):
        # find root and compress path
        # the default parent of i-th table is itself
        # so a symbolic link exits if parents[i] != i

        parents_to_update = []

        # find root
        while root != self.parents[root]:
            parents_to_update.append(self.parents[root])
            root = self.parents[root]

        # compress path
        for i in parents_to_update:
            self.parents[i] = root

        return root


def main():
    n_tables, n_queries = map(int, input().split())
    counts = list(map(int, input().split()))
    assert len(counts) == n_tables

    # n_tables = 6; n_queries = 4
    # counts = [10, 0, 5, 0, 3, 3]
    # test = [(6, 6),
    # (6, 5),
    # (5, 4),
    # (4, 3),]

    db = Database(counts)
    for i in range(n_queries):
        dst, src = map(int, input().split())
        # dst, src = test[i]
        db.merge(dst - 1, src - 1)
        print(db.max_row_count)


if __name__ == "__main__":
    main()
