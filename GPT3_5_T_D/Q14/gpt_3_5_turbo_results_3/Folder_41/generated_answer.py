
def find_second_smallest_num(numbers):
    if len(numbers) < 5:
        return None
    
    numbers = numbers[4:]
    if len(numbers) < 2:
        return None
    
    numbers.sort()
    return numbers[1]
