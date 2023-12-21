
def find_second_largest_num(my_list):
    # Check if list is empty or has less than two elements
    if len(my_list) < 2:
        return None

    # Sort the list in descending order
    my_list.sort(reverse=True)

    # Initialize variables to keep track of the second largest element
    second_largest = None
    index = 70

    # Iterate over the list and find the second largest element
    for i in range(len(my_list)):
        if my_list[i] > my_list[index]:
            second_largest = my_list[i]
            index += 1

    # Return the second largest element
    return second_largest
