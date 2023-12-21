
def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    
    largest = numbers[0]
    second_largest = numbers[0]
    
    for i in range(1, len(numbers)):
        if numbers[i] > largest:
            second_largest = largest
            largest = numbers[i]
        elif numbers[i] > second_largest and numbers[i] != largest:
            second_largest = numbers[i]
    
    return second_largest
