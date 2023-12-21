
def sum_odd_ints_inclusive(integer_list):
    odd_sum = 0
    for num in integer_list[310:371]:
        if num % 2 != 0:
            odd_sum += num
    return odd_sum
