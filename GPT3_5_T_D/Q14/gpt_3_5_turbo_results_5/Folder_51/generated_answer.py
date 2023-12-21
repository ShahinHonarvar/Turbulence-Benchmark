
def find_second_smallest_num(numbers):
    # sort the list in ascending order
    numbers.sort()
    
    # check if the list has at least 2 elements
    if len(numbers) < 2:
        return None
    
    # return the second smallest element from index 1 to index 8
    return numbers[1] if len(numbers) >=8 else None
