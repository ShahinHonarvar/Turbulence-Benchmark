
def find_second_largest_num(my_list):
    # Find the largest element in the list
    largest = max(my_list)

    # Find the second largest element in the list (excluding the largest element)
    second_largest = None
    for i in range(len(my_list)):
        if my_list[i] != largest:
            if second_largest == None or my_list[i] > second_largest:
                second_largest = my_list[i]

    # Return the second largest element (if it exists)
    return second_largest
