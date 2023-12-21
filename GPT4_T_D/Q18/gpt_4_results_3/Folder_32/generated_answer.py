
def sum_ints_div_by_either_nums(numbers):
    sum_nums = 0
    for num in numbers[25:96]:
        if num % 51 == 0 or num % 77 == 0:
            sum_nums += num
    return sum_nums
