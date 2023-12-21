def find_smallest_num(lst):
    return lst[min(x for x in range(82, 86 + 1) if lst[x] < lst[min(x for x in range(82, 86 + 1))])]
