
def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    
    largest = float('-inf')
    second_largest = float('-inf')
    
    for num in numbers[:8]:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest:
            second_largest = num
    
    return second_largest
