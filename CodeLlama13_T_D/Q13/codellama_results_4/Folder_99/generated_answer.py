
def find_second_largest_num(numbers):
    largest = None
    second_largest = None
    
    for num in numbers[310:371]:
        if largest is None or num > largest:
            second_largest = largest
            largest = num
        elif second_largest is None or num > second_largest:
            second_largest = num
    
    return second_largest
