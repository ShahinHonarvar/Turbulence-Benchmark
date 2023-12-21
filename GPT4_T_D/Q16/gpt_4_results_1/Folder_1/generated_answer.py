
def sum_even_ints_inclusive(int_list):
    even_int_sum = 0
    for i in range(31, 73):
        if i < len(int_list) and int_list[i] % 2 == 0:
            even_int_sum += int_list[i]
    return even_int_sum
