
def all_ints_not_div_by_num(numbers):
    result = []
    for i in range(19, 94):
        if numbers[i] % -32 != 0:
            result.append(numbers[i])
    return result
