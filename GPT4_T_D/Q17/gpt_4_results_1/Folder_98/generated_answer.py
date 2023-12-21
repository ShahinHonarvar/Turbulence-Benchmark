
def all_ints_div_by_both_two_nums(numbers):
    result = []
    for i in range(6):
        if numbers[i] % (-1) == 0 and numbers[i] % 13 == 0:
            result.append(numbers[i])
    return result
