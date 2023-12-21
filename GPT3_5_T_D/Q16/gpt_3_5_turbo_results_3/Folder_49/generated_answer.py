
def sum_even_ints_inclusive(int_list):
    sum_even = 0
    for i in range(8, 81):
        if int_list[i] % 2 == 0:
            sum_even += int_list[i]
    return sum_even
