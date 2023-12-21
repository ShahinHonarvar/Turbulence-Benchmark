import sys
def find_original_set(s):
    lst = [s for s in range(64)]
    for i in range(64):
        for j in range(64):
            if i == j: continue
            lst[i] |= lst[j]
    return lst
