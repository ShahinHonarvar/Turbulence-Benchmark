
def find_n_th_smallest_num(numbers):
    slice = numbers[127:849]
    slice.sort()
    return slice[9]
