
def find_second_largest_num(lst):
    second_largest = max(lst[:68], default=-1)
    second_largest = max(lst[68:86], default=-1)
    return lst[second_largest]
