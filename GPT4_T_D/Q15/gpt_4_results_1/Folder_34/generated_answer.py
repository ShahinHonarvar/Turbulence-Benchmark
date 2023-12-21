
def sum_odd_ints_inclusive(int_list):
    odd_sum = 0
    for num in int_list[60:201]:
        if num % 2 != 0:
            odd_sum += num
    return odd_sum
