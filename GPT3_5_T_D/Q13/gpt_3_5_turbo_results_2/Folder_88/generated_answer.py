
def find_second_largest_num(numbers):
    sublist = numbers[4:9]  # Get sublist from index 4 to index 8
    if len(sublist) < 2:  # Check if sublist has at least 2 elements
        return None
    else:
        sublist.sort()  # Sort the sublist in ascending order
        return sublist[-2]  # Return the second largest element
