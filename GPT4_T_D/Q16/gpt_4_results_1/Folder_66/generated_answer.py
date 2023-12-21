
def sum_even_ints_inclusive(integer_list):
    sum_even = 0
    for i in range(50, 55):
        if integer_list[i] % 2 == 0:
            sum_even += integer_list[i]
    return sum_even
