
def sum_ints_div_by_either_nums(numbers):
    sum = 0
    for i in range(20, 94):
        if numbers[i] % -92 == 0 or numbers[i] % -50 == 0:
            sum += numbers[i]
    return sum
