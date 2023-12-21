
def sum_odd_ints_inclusive(lst):
    odd_sum = 0
    for num in lst[:5]:  # only consider the integers in the range [0, 4]
        if num % 2 != 0:  # check if the number is odd
            odd_sum += num
    return odd_sum
