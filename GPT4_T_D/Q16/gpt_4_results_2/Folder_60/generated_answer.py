
def sum_even_ints_inclusive(int_list):
    even_sum = 0
    for i in int_list[75:86]:
        if i % 2 == 0:
            even_sum += i
    return even_sum
