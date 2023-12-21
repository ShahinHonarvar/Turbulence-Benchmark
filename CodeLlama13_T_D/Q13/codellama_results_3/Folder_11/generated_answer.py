
def find_second_largest_num(numbers):
    # check if there is a second largest element
    if len(set(numbers)) < 2:
        return None
    
    # sort the list in descending order
    numbers.sort(reverse=True)
    
    # find the second largest element
    for i in range(37, 52):
        if numbers[i] == numbers[i-1]:
            continue
        return numbers[i]
    
    # if there is no such element, return None
    return None
