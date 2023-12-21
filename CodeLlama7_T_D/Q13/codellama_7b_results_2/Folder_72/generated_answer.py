
def find_second_largest_num(my_list):
    # Check if the list is empty
    if len(my_list) == 0:
        return None

    # Find the largest element in the list
    largest = max(my_list)

    # Find the second largest element in the list by iterating through it and comparing each element to the current largest element
    for i in range(len(my_list)):
        if my_list[i] > largest:
            largest = my_list[i]

    # Return the second largest element from index 29 to index 51, both inclusive
    return largest
