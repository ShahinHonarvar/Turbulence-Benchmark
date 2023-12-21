
def sum_ints_div_by_either_nums(numbers):
    result = 0
    for i in range(80, 201):
        if numbers[i] % 10 == 0 or numbers[i] % 1000 == 0:
            result += numbers[i]
    return result
