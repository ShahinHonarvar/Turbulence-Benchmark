
def find_second_largest_num(numbers):
    if len(numbers) <= 2:
        return None
    
    second_largest = None
    largest = max(numbers[0], numbers[1])
    for i in range(2, 8):
        num = numbers[i]
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and second_largest is not None:
            second_largest = num
    
    return second_largest
