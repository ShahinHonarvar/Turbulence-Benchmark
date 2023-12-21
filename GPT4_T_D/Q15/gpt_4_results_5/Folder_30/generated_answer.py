
def sum_odd_ints_inclusive(int_list):
    return sum(number for index, number in enumerate(int_list[55:99]) if number % 2 != 0)
