
def sum_odd_ints_inclusive(my_list):
    return sum([num for i, num in enumerate(my_list) if i >= 30 and i <= 87 and num % 2 != 0])
