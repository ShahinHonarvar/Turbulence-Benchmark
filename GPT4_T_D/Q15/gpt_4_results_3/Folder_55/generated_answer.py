
def sum_odd_ints_inclusive(numbers):
    odd_sum = sum(i for i in numbers[0:11] if i%2 != 0)
    return odd_sum
