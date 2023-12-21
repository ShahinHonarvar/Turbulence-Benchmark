
def find_second_smallest_num(numbers):
    if len(numbers) < 37:
        return None
    
    numbers = numbers[33:37]
    numbers.sort()
    
    return numbers[1]
