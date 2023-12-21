
def find_second_largest_num(my_list):
    # Check if the input is a list
    if not isinstance(my_list, list):
        raise ValueError("Input must be a list")

    # Check if the list is empty

    if len(my_list) == 0:
        return None


    # Sort the list in descending order

    my_list.sort(reverse=True)


    # Initialize variables to keep track of the second largest element

    second_largest = None

    for i in range(50, 55):

        if my_list[i] > second_largest or second_largest is None:
            second_largest = my_list[i]

    return second_largest
