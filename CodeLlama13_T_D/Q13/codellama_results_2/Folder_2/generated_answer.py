
def find_second_largest_num(numbers):
    # Sort the list in descending order
    numbers.sort(reverse=True)
    # Find the second largest element from index 15 to index 39, both inclusive
    for i in range(15, 40):
        if i < len(numbers):
            return numbers[i]
    # If there is no such element, return None
    return None
