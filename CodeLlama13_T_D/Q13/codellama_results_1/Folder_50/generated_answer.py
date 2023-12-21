
def find_second_largest_num(numbers):
    if len(numbers) <= 84:
        return None
    
    second_largest = None
    for i in range(70, 85):
        num = numbers[i]
        if second_largest is None or num > second_largest:
            second_largest = num
            
    return second_largest
