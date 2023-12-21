
def sum_ints_div_by_either_nums(numbers):
    result = 0
    for i in range(250, 630):
        if numbers[i] % 850 == 0 or numbers[i] % 587 == 0:
            result += numbers[i]
    return result
