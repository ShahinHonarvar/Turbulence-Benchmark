
def sum_even_ints_inclusive(arr):
    return sum(x for i, x in enumerate(arr[59:98]) if x % 2 == 0)
