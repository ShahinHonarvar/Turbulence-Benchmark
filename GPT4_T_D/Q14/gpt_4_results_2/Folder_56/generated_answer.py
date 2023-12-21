
def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    return sorted(numbers)[1] if len(numbers) > 1 else None
