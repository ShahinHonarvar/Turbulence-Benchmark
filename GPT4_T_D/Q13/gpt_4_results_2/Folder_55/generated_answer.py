
def find_second_largest_num(numbers):
    num_subset = numbers[:11]
    if len(num_subset) <= 1:
        return None
    else:
        num_subset.sort()
        return num_subset[-2]
