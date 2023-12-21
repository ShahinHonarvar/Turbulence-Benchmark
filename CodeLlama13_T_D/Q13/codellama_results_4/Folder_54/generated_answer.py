
def find_second_largest_num(numbers):
    # Get the second largest element from index 34 to index 55, both inclusive
    second_largest = sorted(numbers[34:56])[-2]
    
    # If there is no such element, return 'None'
    if second_largest == None:
        return 'None'
    else:
        return second_largest
