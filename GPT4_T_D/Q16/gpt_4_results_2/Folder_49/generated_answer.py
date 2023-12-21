
def sum_even_ints_inclusive(integers_list):
    even_sum = 0
    for i in range(8, min(81, len(integers_list))):
        if integers_list[i] % 2 == 0:
            even_sum += integers_list[i]
    return even_sum
