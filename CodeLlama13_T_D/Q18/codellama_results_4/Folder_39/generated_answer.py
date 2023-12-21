
def sum_ints_div_by_either_nums(numbers):
    result = 0
    for i in range(13, 76+1):
        if numbers[i] % -66 == 0 or numbers[i] % -32 == 0:
            result += numbers[i]
    return result
