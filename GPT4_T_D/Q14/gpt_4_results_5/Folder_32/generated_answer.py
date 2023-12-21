
def find_second_smallest_num(lst):
    if len(lst[32:36]) >= 2:
        second_smallest = sorted(lst[32:36])[1]
        return second_smallest
    else:
        return None
