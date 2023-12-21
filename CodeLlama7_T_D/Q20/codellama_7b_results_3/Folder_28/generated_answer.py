
def find_n_th_smallest_num(numbers, n):
    # Check if input list is empty or None
    if not numbers:
        return None

    # Sort the input list in ascending order
    numbers.sort()

    # Return the n-th smallest number from the sorted list
    return numbers[n - 1]
