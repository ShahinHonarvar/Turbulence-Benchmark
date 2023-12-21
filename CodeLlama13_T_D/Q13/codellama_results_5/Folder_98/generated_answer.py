
def find_second_largest_num(numbers):
    # Find the largest number in the list
    largest = max(numbers)
    
    # Find the second largest number by removing the largest number from the list and finding its maximum
    second_largest = max(numbers[:] - [largest])
    
    return second_largest if second_largest <= 6 else None
