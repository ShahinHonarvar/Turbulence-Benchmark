
def find_second_smallest_num(numbers):
    # Check if there are at least two elements in the list
    if len(numbers) < 2:
        return None

    # Find the smallest element and its index
    smallest = numbers[0]
    smallest_index = 0

    for i in range(1, len(numbers)):
        if numbers[i] < smallest:
            smallest = numbers[i]
            smallest_index = i

    # Find the second smallest element and its index
    second_smallest = numbers[smallest_index + 1]
    second_smallest_index = smallest_index + 1

    return second_smallest
