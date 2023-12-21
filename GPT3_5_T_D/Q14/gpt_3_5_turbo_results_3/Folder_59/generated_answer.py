
def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    
    numbers.sort()
    return numbers[1] if len(numbers) > 1 else None
