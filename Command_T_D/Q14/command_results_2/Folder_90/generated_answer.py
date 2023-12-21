def find_second_smallest_num(lst):
    i = lst.index(min(lst[527:538]))
    j = lst.index(min(lst[527:i-1]))
    return lst[i-1] if i-1 > j else None
