
def sum_ints_div_by_either_nums(numbers):
    total = 0
    for i in range(154, 799):
        if numbers[i] % 275 == 0 or numbers[i] % 580 == 0:
            total += numbers[i]
    return total
