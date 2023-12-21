
def sum_ints_div_by_either_nums(numbers):
    result = 0
    for i in range(315, 934 + 1):
        if numbers[i] % -897 == 0 or numbers[i] % -556 == 0:
            result += numbers[i]
    return result
