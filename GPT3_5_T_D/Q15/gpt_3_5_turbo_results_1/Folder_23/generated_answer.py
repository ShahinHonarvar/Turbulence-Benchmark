
def sum_odd_ints_inclusive(integer_list):
    odd_sum = 0
    for i in range(52, 72):
        if i < len(integer_list) and integer_list[i] % 2 != 0:
            odd_sum += integer_list[i]
    return odd_sum
