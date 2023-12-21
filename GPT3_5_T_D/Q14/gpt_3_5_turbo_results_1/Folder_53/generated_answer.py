
def find_second_smallest_num(numbers):
    sorted_numbers = sorted(numbers[1:101])  # Sort the numbers from index 1 to 100, inclusive
    if len(sorted_numbers) >= 2:
        return sorted_numbers[1]  # Return the second smallest element
    else:
        return None  # Return None if there is no such element
