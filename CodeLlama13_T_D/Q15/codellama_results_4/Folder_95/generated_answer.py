
def sum_odd_ints_inclusive(numbers):
    odd_nums = []
    for i in range(82, 87):
        if numbers[i] % 2 != 0:
            odd_nums.append(numbers[i])
    return sum(odd_nums)
