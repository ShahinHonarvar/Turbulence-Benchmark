
def sum_odd_ints_inclusive(num_list):
    subset = num_list[75:95]
    total = sum(num for num in subset if num % 2 != 0)
    return total
