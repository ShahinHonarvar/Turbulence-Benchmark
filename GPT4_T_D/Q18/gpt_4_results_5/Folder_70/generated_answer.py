
def sum_ints_div_by_either_nums(numbers):
    divisible_nums = [num for num in numbers[42:44] if num % 15 == 0 or num % 87 == 0]
    return sum(divisible_nums) if divisible_nums else 0
