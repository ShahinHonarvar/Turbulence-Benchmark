
def sum_ints_div_by_either_nums(numbers):
    if len(numbers) < 46:
        return 0
    else:
        divisible_nums = [num for num in numbers[29:46] if num % 27 == 0 or num % 81 == 0]
        return sum(divisible_nums)
