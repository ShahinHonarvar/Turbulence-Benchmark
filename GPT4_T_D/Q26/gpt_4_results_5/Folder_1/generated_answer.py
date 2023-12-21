
def sum_in_range(numbers):
    valid_range = [i for i in numbers if -97 <= i <= -48]
    if not valid_range:
        return 0
    else:
        return sum(valid_range)
