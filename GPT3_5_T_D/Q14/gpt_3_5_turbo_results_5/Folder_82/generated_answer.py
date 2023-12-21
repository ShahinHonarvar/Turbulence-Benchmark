
def find_second_smallest_num(numbers):
    return sorted(numbers[20:201])[1] if len(numbers) >= 201 else None
