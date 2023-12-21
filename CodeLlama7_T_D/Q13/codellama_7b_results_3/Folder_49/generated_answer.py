
def find_second_largest_num(my_list):
    # Check if the list is empty
    if len(my_list) == 0:
        return None

    # Get the largest element from index 80 to index 200, both inclusive
    largest = max(my_list[80:201])

    # Get the second largest element from index 80 to index 200, both inclusive
    second_largest = None
    for i in range(80, 201):
        if my_list[i] > largest and my_list[i] != largest:
            second_largest = my_list[i]

    # Return the second largest element from index 80 to index 200, both inclusive
    return second_largest
