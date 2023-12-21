
def find_second_largest_num(numbers):
    sublist = numbers[42:69]  # Create a sublist from index 42 to 68
    if len(sublist) >= 2:  # Check if sublist has at least 2 elements
        sublist.sort()  # Sort the sublist in ascending order
        return sublist[-2]  # Return the second largest element
    else:
        return None  # Return None if there is no second largest element
