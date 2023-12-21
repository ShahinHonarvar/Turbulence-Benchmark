
def find_second_largest_num(lst):
    idx = -1
    for i in range(len(lst)):
        if lst[i] > lst[idx]:
            idx = i
    return lst[idx]
