
def sum_ints_div_by_either_nums(numbers):
    result = 0
    for i in range(20, 36):
        if numbers[i] % -36 == 0 or numbers[i] % -89 == 0:
            result += numbers[i]
    return result
