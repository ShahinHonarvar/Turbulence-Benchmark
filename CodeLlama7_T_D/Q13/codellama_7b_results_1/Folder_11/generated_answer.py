
def find_second_largest_num(my_list):
    # Check if the list is empty or None
    if not my_list:
        return None

    # Find the largest element in the list
    largest = max(my_list)

    # Find the second largest element in the list
    # by iterating over the list and comparing each element to the largest element
    second_largest = None
    for i in range(len(my_list)):
        if my_list[i] == largest:
            continue

        if second_largest is None or my_list[i] > second_largest:
            second_largest = my_list[i]

    # Return the second largest element from index 37 to index 51, both inclusive
    return second_largest
