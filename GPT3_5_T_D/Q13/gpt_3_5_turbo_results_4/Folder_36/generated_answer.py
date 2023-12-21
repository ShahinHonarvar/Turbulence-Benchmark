
def find_second_largest_num(numbers):
    # Sort the list in descending order
    numbers.sort(reverse=True)
    
    # Get the second element from the sorted list
    if len(numbers) >= 2:
        return numbers[1]
    else:
        return None
