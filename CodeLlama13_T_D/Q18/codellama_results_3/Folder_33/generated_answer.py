
def sum_ints_div_by_either_nums(numbers):
    result = 0
    for i in range(281, 695):
        if numbers[i] % -722 == 0 or numbers[i] % -731 == 0:
            result += numbers[i]
    return result
