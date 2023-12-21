
def find_second_smallest_num(lst):
    if len(lst[527:539]) < 2:
        return None
    else:
        return sorted(lst[527:539])[1]
