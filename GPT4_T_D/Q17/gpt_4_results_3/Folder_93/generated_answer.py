
def all_ints_div_by_both_two_nums(numbers):
    result = []
    for i in range(86, 90):
        if i < len(numbers) and numbers[i] % -61 == 0 and numbers[i] % -79 == 0:
            result.append(numbers[i])
    return result
