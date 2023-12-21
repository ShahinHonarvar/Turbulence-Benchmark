
def sum_ints_div_by_either_nums(numbers):
    result = 0
    for i in range(31, 51):
        if numbers[i] % 81 == 0 or numbers[i] % 64 == 0:
            result += numbers[i]
    return result
