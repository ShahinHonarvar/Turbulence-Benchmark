
def find_second_smallest_num(numbers):
    if len(numbers) == 2:
        return max(numbers)
    elif len(numbers) > 2:
        first_three_numbers = sorted(numbers[:3])
        return first_three_numbers[1]
    else:
        return None
