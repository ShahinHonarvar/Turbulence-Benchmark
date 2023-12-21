
def sum_odd_ints_inclusive(int_list):
    range_subset = int_list[29:94]
    odd_integers = [num for num in range_subset if num % 2 != 0]
    return sum(odd_integers) if odd_integers else 0
