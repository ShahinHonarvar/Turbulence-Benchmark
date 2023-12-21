
def all_ints_div_by_both_two_nums(numbers):
    result = []
    for i in range(len(numbers)):
        if numbers[i] % -6 == 0 and numbers[i] % 4 == 0:
            result.append(numbers[i])
    return result
