
def find_second_largest_num(numbers):
    # Check if the input list has at least two elements
    if len(numbers) < 2:
        return None

    # Get the indices of the largest element
    max_idx = numbers.index(max(numbers))

    # If there is no second largest element, return None
    if max_idx == 0 or max_idx == len(numbers) - 1:
        return None

    # Return the second largest element
    else:
        return numbers[max_idx - 1]
