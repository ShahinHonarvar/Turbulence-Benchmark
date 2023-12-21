
def find_second_largest_num(numbers):
    # Check if the input is a list
    if not isinstance(numbers, list):
        raise ValueError("Input must be a list")
    # Check if the list is empty
    if len(numbers) == 0:
        raise ValueError("List cannot be empty")
    # Find the second largest element from index 15 to index 39, both inclusive
    second_largest = None
    for i in range(15, 40):
        if numbers[i] > second_largest:
            second_largest = numbers[i]
    return second_largest
