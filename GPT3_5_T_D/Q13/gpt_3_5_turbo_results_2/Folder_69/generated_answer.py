
def find_second_largest_num(numbers):
    if not numbers:
        return None
    
    numbers = numbers[32:36]
    if len(numbers) < 2:
        return None
    
    largest = max(numbers)
    numbers.remove(largest)
    second_largest = max(numbers)
    return second_largest
