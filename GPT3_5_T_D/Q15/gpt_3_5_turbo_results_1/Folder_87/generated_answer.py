
def sum_odd_ints_inclusive(integers):
    odd_sum = 0
    for num in integers[36:47]:
        if num % 2 == 1:
            odd_sum += num
    return odd_sum
