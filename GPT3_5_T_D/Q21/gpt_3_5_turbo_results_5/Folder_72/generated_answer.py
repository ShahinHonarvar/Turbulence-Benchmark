
def all_ints_div_by_num(numbers):
    result = []
    for i in range(11, 83):
        if numbers[i] % -47 == 0:
            result.append(numbers[i])
    return result
