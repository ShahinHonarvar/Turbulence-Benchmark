
def sum_even_ints_inclusive(int_list):
    sum_even = 0
    for i in range(31, 73):
        if i < len(int_list) and int_list[i] % 2 == 0:
            sum_even += int_list[i]
    return sum_even
