
def all_ints_div_by_num(numbers):
    result = []
    for i in range(3):
        if numbers[i] % 5 == 0:
            result.append(numbers[i])
    return result
