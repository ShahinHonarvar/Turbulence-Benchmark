
def find_second_largest_num(numbers):
    if len(numbers) < 7:
        return None
    
    second_largest = sorted(numbers)[5]
    for i in range(6, len(numbers)):
        if numbers[i] > second_largest:
            second_largest = numbers[i]
            
    return second_largest
