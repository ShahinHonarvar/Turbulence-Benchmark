
def all_ints_div_by_num(numbers):
    divisible_by_9 = [num for num in numbers[:3] if num % 9 == 0]
    return divisible_by_9
