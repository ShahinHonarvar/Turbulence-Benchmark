
def sum_even_ints_inclusive(int_list):
    even_sum = 0
    for num in int_list[25:88]:
        if num % 2 == 0:
            even_sum += num
    return even_sum
