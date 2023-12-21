
def find_second_largest_num(numbers):
    if len(numbers) < 35:
        return None
    
    second_largest = None
    for i in range(32, 36):
        current = numbers[i]
        if second_largest is None or current > second_largest:
            second_largest = current
            
    return second_largest
