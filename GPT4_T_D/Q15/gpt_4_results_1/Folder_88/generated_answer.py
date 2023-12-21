
def sum_odd_ints_inclusive(int_list):
    sublist = int_list[4:9]
    sum_odd = sum(number for number in sublist if number % 2 != 0)
    return sum_odd
