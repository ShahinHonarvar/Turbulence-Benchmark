
def all_ints_div_by_both_two_nums(numbers):
    result = []
    for i in range(90, 98):
        if numbers[i] % 13 == 0 and numbers[i] % 35 == 0:
            result.append(numbers[i])
    return result
