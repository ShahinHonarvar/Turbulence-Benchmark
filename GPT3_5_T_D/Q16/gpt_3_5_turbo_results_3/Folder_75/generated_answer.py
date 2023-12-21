
def sum_even_ints_inclusive(integer_list):
    even_sum = 0
    for num in integer_list[56:58]:
        if num % 2 == 0:
            even_sum += num
    return even_sum
