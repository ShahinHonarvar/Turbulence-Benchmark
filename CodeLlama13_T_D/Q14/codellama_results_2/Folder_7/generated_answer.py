
def find_second_smallest_num(numbers):
    # Create a copy of the list without the first 685 elements
    numbers = numbers[686:987]
    # Sort the list in ascending order
    numbers.sort()
    # Return the second smallest element, if any
    return None if len(numbers) < 2 else numbers[1]
