
def sum_ints_div_by_either_nums(numbers):
    if len(numbers) < 35:
        return 0
    sum = 0
    for i in range(20, 36):
        num = numbers[i]
        if num % -36 == 0 or num % -89 == 0:
            sum += num
    return sum
