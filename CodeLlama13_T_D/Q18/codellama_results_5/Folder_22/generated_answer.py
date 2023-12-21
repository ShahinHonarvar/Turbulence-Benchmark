
def sum_ints_div_by_either_nums(numbers):
    sum = 0
    for i in range(40, 201):
        if numbers[i] % 21 == 0 or numbers[i] % 71 == 0:
            sum += numbers[i]
    return sum
