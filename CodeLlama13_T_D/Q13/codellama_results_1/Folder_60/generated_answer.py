
def find_second_largest_num(numbers):
    # find the second largest element in the list
    second_largest = None
    for i in range(75, 86):
        if numbers[i] > second_largest:
            second_largest = numbers[i]
    
    return second_largest
