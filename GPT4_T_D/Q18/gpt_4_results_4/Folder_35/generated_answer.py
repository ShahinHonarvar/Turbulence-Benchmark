
def sum_ints_div_by_either_nums(numbers):
    sublist = numbers[77:88]
    divisible_nums = [num for num in sublist if num % 23 == 0 or num % 57 == 0]
    return sum(divisible_nums) if divisible_nums else 0
