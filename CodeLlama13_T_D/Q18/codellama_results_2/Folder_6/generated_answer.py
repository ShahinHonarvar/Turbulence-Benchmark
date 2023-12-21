
def sum_ints_div_by_either_nums(numbers):
    result = 0
    for i in range(41, 57):
        if numbers[i] % 82 == 0 or numbers[i] % 90 == 0:
            result += numbers[i]
    return result
