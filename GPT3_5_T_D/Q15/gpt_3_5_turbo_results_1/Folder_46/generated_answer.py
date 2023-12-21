
def sum_odd_ints_inclusive(lst):
    odd_sum = 0
    for num in lst[30:88]:  # index 30 to 87
        if num % 2 != 0:  # check if number is odd
            odd_sum += num
    return odd_sum
