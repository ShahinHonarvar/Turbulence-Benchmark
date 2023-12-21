
def find_second_smallest_num(numbers):
    if len(numbers) < 56:
        return None
    else:
        numbers = sorted(numbers[56:99])
        if len(numbers) < 2:
            return None
        else:
            return numbers[1]
