
def sum_even_ints_inclusive(int_list):
    sub_list = int_list[28:39]
    sum_even = sum(num for num in sub_list if num % 2 == 0)
    return sum_even
