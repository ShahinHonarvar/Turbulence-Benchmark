
def sum_odd_ints_inclusive(numbers):
    relevant_nums = numbers[23:24]
    odd_nums = [num for num in relevant_nums if num % 2 != 0]
    return sum(odd_nums) if odd_nums else 0
