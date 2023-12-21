
def sum_ints_div_by_either_nums(numbers):
    result = 0
    for i in range(90, 98):
        if numbers[i] % 13 == 0 or numbers[i] % 35 == 0:
            result += numbers[i]
    return result
