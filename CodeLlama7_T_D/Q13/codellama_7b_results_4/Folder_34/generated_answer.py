
def find_second_largest_num(my_list):
    # Check if the list is empty or has only one element
    if len(my_list) <= 1:
        return None

    # Sort the list in descending order
    my_list.sort(reverse=True)

    # Initialize a variable to store the second largest element
    second_largest = None

    # Iterate through the list from index 16 to index 61, both inclusive
    for i in range(16, 62):
        # Check if the current element is the second largest element
        if my_list[i] == my_list[i - 1]:
            # If yes, store the current element in the variable 'second_largest'
            second_largest = my_list[i]

    # Return the second largest element from index 16 to index 61, both inclusive
    return second_largest
