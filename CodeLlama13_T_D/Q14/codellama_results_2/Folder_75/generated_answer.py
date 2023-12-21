
def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    
    sorted_numbers = sorted(numbers)
    for i in range(12, 93):
        if sorted_numbers[i] != sorted_numbers[i - 1]:
            return sorted_numbers[i]
    
    return None
