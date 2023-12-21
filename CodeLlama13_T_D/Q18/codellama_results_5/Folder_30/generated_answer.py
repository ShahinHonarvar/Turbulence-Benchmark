
def sum_ints_div_by_either_nums(numbers):
    result = 0
    for i in range(11, 76+1):
        if numbers[i] % -81 == 0 or numbers[i] % -94 == 0:
            result += numbers[i]
    return result
