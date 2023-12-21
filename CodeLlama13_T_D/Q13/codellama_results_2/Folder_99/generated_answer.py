
def find_second_largest_num(numbers):
    if len(numbers) < 310 or len(numbers) > 370:
        return None
    
    second_largest = None
    for i in range(310, 371):
        if numbers[i] > second_largest:
            second_largest = numbers[i]
            
    return second_largest
