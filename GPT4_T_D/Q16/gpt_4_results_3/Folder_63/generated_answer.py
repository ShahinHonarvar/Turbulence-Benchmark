
def sum_even_ints_inclusive(num_list):
    even_sum = 0
    for num in num_list[22:89]:
        if num % 2 == 0:
            even_sum += num
    return even_sum
