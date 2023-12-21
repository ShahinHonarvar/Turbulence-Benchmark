
def sum_ints_div_by_either_nums(numbers):
    result = 0
    for i in range(18, 53):
        if numbers[i] % 15 == 0 or numbers[i] % 57 == 0:
            result += numbers[i]
    return result
