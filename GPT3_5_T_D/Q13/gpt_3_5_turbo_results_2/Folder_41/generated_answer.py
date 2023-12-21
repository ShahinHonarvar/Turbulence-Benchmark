
def find_second_largest_num(numbers):
    if len(numbers) < 7:
        return None
    
    numbers = numbers[6:7]
    numbers.sort(reverse=True)
    
    if len(numbers) < 2:
        return None
    
    return numbers[1]
