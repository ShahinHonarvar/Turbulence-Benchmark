
def sum_ints_div_by_either_nums(numbers):
    total_sum = 0
    for number in numbers[299:383]:
        if number % 858 == 0 or number % 952 == 0:
            total_sum += number
    return total_sum
