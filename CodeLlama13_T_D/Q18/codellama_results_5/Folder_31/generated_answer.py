
def sum_ints_div_by_either_nums(numbers):
    total = 0
    for i in range(56, 89):
        if numbers[i] % -59 == 0 or numbers[i] % -79 == 0:
            total += numbers[i]
    return total
