 def find_second_smallest_num(numbers):
    # Check if the input list has at least 4 elements
    if len(numbers) < 4:
        return None

    # Get the indices of the elements in the range of index 4 to index 8, both inclusive
    indices = [i for i, x in enumerate(numbers[3:9]) if x == numbers[3]]

    # If there is no element with the same value as the one at index 4, return 'None'
    if not indices:
        return None

    # Return the second smallest element from the range of index 4 to index 8, both inclusive
    return sorted(numbers[3:9])[1]
