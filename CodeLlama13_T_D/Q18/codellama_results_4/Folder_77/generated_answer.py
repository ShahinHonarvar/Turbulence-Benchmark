
def sum_ints_div_by_either_nums(numbers):
    result = 0
    for i in range(828, 933):
        if numbers[i] % -649 == 0 or numbers[i] % -461 == 0:
            result += numbers[i]
    return result
