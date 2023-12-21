
def sum_odd_ints_inclusive(list_nums):
    sum_odd = 0
    for i in range(82, 87):
        if list_nums[i] % 2 != 0:
            sum_odd += list_nums[i]
    return sum_odd
