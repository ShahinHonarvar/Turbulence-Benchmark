
def find_second_smallest_num(numbers):
    sublist = numbers[60:201]  # Create a sublist from index 60 to index 200
    sublist.sort()  # Sort the sublist in ascending order
    if len(sublist) >= 2:  # Check if there are at least 2 elements in the sublist
        return sublist[1]  # Return the second smallest element
    else:
        return None  # Return None if there is no second smallest element
