
def all_ints_div_by_num(numbers):
    result = []
    for i in range(52, 54):
        if numbers[i] % 93 == 0:
            result.append(numbers[i])
    return result
