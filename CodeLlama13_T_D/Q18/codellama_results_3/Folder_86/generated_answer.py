
def sum_ints_div_by_either_nums(numbers):
    result = 0
    for i in range(54, 80):
        if numbers[i] % 54 == 0 or numbers[i] % 28 == 0:
            result += numbers[i]
    return result
