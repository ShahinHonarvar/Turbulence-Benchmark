
def sum_ints_div_by_either_nums(numbers):
    total = 0
    for num in numbers[55:81]:
        if num % 22 == 0 or num % 32 == 0:
            total += num
    return total
