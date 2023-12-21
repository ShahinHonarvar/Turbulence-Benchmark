
def find_second_largest_num(numbers):
    # Check if the input is a list
    if not isinstance(numbers, list):
        raise ValueError("Input must be a list")
    # Check if the list has at least 30 elements
    if len(numbers) < 30:
        raise ValueError("List must have at least 30 elements")
    # Initialize variables to keep track of the largest and second largest elements
    largest = None
    second_largest = None

    # Iterate through the list and find the largest and second largest elements
    for i in range(15, 39 + 1):
        current = numbers[i]
        if largest is None or current > largest:
            second_largest = largest
            largest = current
        elif second_largest is None or current > second_largest:
            second_largest = current

    # Return the second largest element from index 15 to index 39, both inclusive. If there is no such element, return 'None'
    if second_largest is not None:
        return second_largest
    else:
        return None
