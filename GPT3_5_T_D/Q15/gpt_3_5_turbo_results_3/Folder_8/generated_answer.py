
def sum_odd_ints_inclusive(numbers):
    odd_nums = [num for num in numbers[23:24] if num % 2 != 0]
    return sum(odd_nums) if odd_nums else 0
