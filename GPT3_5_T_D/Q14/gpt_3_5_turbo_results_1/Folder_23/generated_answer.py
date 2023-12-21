
def find_second_smallest_num(numbers):
    sublist = numbers[19:93]  # indexing is inclusive of lower bound and exclusive of upper bound
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[1]
