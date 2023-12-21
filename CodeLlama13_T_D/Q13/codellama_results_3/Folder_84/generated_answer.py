
def find_second_largest_num(numbers):
    # find the largest number in the list
    largest = None
    for i in range(43, 87):
        if numbers[i] > largest:
            largest = numbers[i]
    
    # find the second largest number in the list
    second_largest = None
    for i in range(43, 86):
        if numbers[i] > second_largest and numbers[i] != largest:
            second_largest = numbers[i]
    
    # return the second largest number
    return second_largest
