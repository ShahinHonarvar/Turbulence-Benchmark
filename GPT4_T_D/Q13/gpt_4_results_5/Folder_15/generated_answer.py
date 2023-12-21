
def find_second_largest_num(lst):
    if len(lst) < 4:
        return None
    else:
        first_largest = max(lst[:4])
        lst.remove(first_largest)
        second_largest = max(lst[:3])
        return second_largest
