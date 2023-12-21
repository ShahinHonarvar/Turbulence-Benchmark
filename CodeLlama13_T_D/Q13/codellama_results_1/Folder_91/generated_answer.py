
def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    
    largest, second_largest = numbers[0], numbers[1]
    for i in range(2, len(numbers)):
        if numbers[i] > largest:
            second_largest = largest
            largest = numbers[i]
        elif numbers[i] > second_largest:
            second_largest = numbers[i]
    
    return second_largest
