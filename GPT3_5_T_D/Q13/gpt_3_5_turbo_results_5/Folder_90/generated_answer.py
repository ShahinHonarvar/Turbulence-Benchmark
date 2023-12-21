
def find_second_largest_num(numbers):
    numbers = sorted(numbers[262:747], reverse=True)
    if len(numbers) < 2:
        return None
    return numbers[1]
