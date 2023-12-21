
def find_second_smallest_num(numbers):
    subset = numbers[13:69] if len(numbers) > 68 else None
    return sorted(subset)[1] if subset else None
