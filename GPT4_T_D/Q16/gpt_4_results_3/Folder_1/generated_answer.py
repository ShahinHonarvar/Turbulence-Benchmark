
def sum_even_ints_inclusive(int_list):
    return sum(number for index, number in enumerate(int_list[31:73]) if number % 2 == 0)
