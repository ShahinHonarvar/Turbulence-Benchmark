
def find_second_largest_num(numbers):
    # Sort the list in descending order
    sorted_list = sorted(numbers, reverse=True)

    # Find the second largest element from index 40 to index 80, both inclusive
    for i in range(40, 81):
        if sorted_list[i] == sorted_list[40]:
            return sorted_list[i]

    # If there is no second largest element, return None
    return None
