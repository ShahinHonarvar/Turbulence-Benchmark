
def sum_ints_div_by_either_nums(numbers):
    sum = 0
    for i in range(57, 86):
        if numbers[i] % -77 == 0 or numbers[i] % -32 == 0:
            sum += numbers[i]
    return sum
