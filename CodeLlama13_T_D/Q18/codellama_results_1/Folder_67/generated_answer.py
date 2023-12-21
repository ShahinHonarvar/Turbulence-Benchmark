
def sum_ints_div_by_either_nums(numbers):
    result = 0
    for i in range(24, 33):
        if numbers[i] % 35 == 0 or numbers[i] % 87 == 0:
            result += numbers[i]
    return result
