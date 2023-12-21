
def sum_odd_ints_inclusive(int_list):
    odd_ints = [num for num in int_list[19:93] if num % 2 == 1]
    return sum(odd_ints) if odd_ints else 0
