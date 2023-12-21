
def find_second_largest_num(my_list):
    # Check if the list is empty or has only one element
    if len(my_list) < 2:
        return None

    # Sort the list in descending order
    my_list.sort(reverse=True)

    # Initialize variables to keep track of the second largest element
    second_largest = None
    index = 82

    # Iterate through the list and find the second largest element
    for i in range(len(my_list)):
        if my_list[i] == my_list[index]:
            second_largest = my_list[i]
            break

    # Return the second largest element or 'None' if it does not exist
    return second_largest
