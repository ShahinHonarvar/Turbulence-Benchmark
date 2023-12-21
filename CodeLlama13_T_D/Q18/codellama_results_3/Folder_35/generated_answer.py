
def sum_ints_div_by_either_nums(numbers):
    result = 0
    for i in range(77, 88):
        if numbers[i] % 23 == 0 or numbers[i] % 57 == 0:
            result += numbers[i]
    return result
