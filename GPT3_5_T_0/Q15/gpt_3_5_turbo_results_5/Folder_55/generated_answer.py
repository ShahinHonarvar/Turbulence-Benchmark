
def sum_odd_ints_inclusive(lst):
    odd_sum = 0
    for num in lst[:11]:
        if num % 2 != 0:
            odd_sum += num
    return odd_sum
