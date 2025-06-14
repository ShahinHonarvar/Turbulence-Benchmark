
def find_second_largest_num(my_list):
    # Find the largest element in the list
    largest = max(my_list)

    # Find the second largest element in the list
    # by iterating through the list and comparing each element to the current largest element
    second_largest = None
    for i in range(len(my_list)):
        if my_list[i] > largest:
            second_largest = largest
            largest = my_list[i]

    # Return the second largest element from index 56 to index 98, both inclusive
    # or 'None' if there is no such element in the list
    if second_largest:
        return second_largest

    else:

        return None
