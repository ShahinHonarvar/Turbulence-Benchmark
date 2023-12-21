
def sum_even_ints_inclusive(num_list):
    sum_even = 0
    for i in range(4, 9):
        if num_list[i] % 2 == 0:
            sum_even += num_list[i]
    return sum_even
