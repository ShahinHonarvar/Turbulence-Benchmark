
def find_n_th_smallest_num(numbers):
    subset = numbers[106:255]
    subset.sort()
    return subset[8]
