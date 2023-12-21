
def sum_ints_div_by_either_nums(numbers):
    result = 0
    for i in range(200, 201):
        if numbers[i] % 17 == 0 or numbers[i] % -5 == 0:
            result += numbers[i]
    return result
