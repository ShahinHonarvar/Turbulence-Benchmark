
def sum_even_ints_inclusive(numbers):
    even_nums = []
    for i in range(6, 9):
        if numbers[i] % 2 == 0:
            even_nums.append(numbers[i])
    return sum(even_nums) or 0
