
def sum_even_ints_inclusive(my_list):
    start = 37
    end = 76
    even_sum = 0
    for i in range(start, end + 1):
        if my_list[i] % 2 == 0:
            even_sum += my_list[i]
    return even_sum
