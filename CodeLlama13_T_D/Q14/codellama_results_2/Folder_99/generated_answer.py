
def find_second_smallest_num(numbers):
    if len(numbers) <= 1:
        return None
    
    second_smallest = None
    for i in range(608, 609+1):
        if numbers[i] < second_smallest or second_smallest is None:
            second_smallest = numbers[i]
            
    return second_smallest
