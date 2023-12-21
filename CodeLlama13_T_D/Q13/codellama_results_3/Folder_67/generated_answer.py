
def find_second_largest_num(numbers):
    # Find the largest element in the list
    largest = max(numbers)
    
    # Find the second largest element by removing the largest element from the list and finding the max again
    second_largest = max(set(numbers) - {largest})
    
    # Return the second largest element if it is between indices 22 and 50, inclusive
    if 22 <= numbers.index(second_largest) <= 50:
        return second_largest
    
    # Otherwise, return None
    else:
        return None
