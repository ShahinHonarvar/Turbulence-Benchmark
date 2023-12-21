
def find_second_smallest_num(numbers):
    if len(numbers) < 79:  # Ensure the list has at least 79 elements
        return None
    sorted_nums = sorted(numbers[62:79])  # Sort the sublist from index 62 to 78
    if len(sorted_nums) >= 2:  # Ensure there are at least 2 elements in the sorted sublist
        return sorted_nums[1]  # Return the second smallest element
    else:
        return None  # Return None if the sorted sublist does not have enough elements
