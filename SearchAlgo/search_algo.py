#%%
import numpy as np
import itertools

mat = np.array([
    [0, 1, 0, 1, 0],
    [0, 1, 0, 1, 1],
    [0, 0, 0, 0, 1],
    [0, 1, 1, 0, 1],
    [0, 1, 0, 0, 0],
])


# depth-first search
path_list = []
visit_mat = np.zeros((5, 5), dtype=bool)
flag = False

def dfs(i, j, flag):

    visit_mat[i, j] = True

    if flag == True:
        return path_list

    if i == 4 and j == 4:
        flag = True
        return None

    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:

        next_i = i + di
        next_j = j + dj
        if next_i < 0 or next_j < 0 or next_i > 4 or next_j > 4:
            continue       
        if mat[next_i, next_j] == 0 and visit_mat[next_i, next_j] == False:
            search_flag = True
            dfs(next_i, next_j, flag)


dfs(0, 0, False)

print(visit_mat)


# %%
