
def find_second_largest_num(my_list):
    # Find the largest element in the list
    largest = max(my_list)

    # Find the second largest element in the list
    second_largest = None
    for i in range(43, 86 + 1):
        if my_list[i] > second_largest:
            second_largest = my_list[i]

    # Return the second largest element from index 43 to index 86, both inclusive
    return second_largest
