
def all_ints_div_by_both_two_nums(numbers):
    result = []
    for i in range(10, 76 + 1):
        if numbers[i] % -40 == 0 and numbers[i] % -12 == 0:
            result.append(numbers[i])
    return result
