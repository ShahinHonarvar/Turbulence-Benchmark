
def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    
    largest = numbers[0]
    second_largest = None
    for i in range(1, len(numbers)):
        num = numbers[i]
        if num > largest:
            second_largest = largest
            largest = num
        elif second_largest is None or num > second_largest:
            second_largest = num
    
    return second_largest
