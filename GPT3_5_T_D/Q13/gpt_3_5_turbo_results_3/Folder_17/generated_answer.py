
def find_second_largest_num(numbers):
    numbers.sort()
    if len(numbers) < 63 or len(numbers) <= 78:
        return None
    return numbers[-2]
