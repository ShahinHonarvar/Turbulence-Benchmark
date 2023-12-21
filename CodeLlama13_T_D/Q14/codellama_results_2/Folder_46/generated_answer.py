
def find_second_smallest_num(numbers):
    # Sort the list in ascending order
    numbers.sort()
    # Find the second smallest element from index 13 to index 68, both inclusive
    for i in range(13, 69):
        if numbers[i] < numbers[i-1]:
            return numbers[i]
    # If there is no such an element, return None
    return None
