
def sum_ints_div_by_either_nums(numbers):
    result = 0
    for i in range(543, 585):
        if numbers[i] % -553 == 0 or numbers[i] % -737 == 0:
            result += numbers[i]
    return result
