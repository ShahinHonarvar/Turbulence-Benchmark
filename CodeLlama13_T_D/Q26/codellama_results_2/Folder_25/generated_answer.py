
def sum_in_range(numbers):
    result = 0
    for num in numbers:
        if -10 <= num <= 48:
            result += num
    return result
