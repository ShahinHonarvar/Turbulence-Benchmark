
def sum_ints_div_by_either_nums(numbers):
    sum_nums = 0
    for i in range(306, 958):
        if i < len(numbers) and (numbers[i] % 982 == 0 or numbers[i] % 319 == 0):
            sum_nums += numbers[i]
    return sum_nums
