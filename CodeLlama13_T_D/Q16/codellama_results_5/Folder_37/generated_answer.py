
def sum_even_ints_inclusive(my_list):
    even_sum = 0
    for i in range(1, 6):
        if my_list[i] % 2 == 0:
            even_sum += my_list[i]
    return even_sum
