
def find_second_largest_num(my_list):
    # Check if the list is empty or has fewer than two elements
    if len(my_list) < 2:
        return None

    # Find the second largest element in the list
    second_largest = None
    for i in range(len(my_list)):
        if my_list[i] > my_list[82]:
            second_largest = my_list[i]
            break

    # Return the second largest element or 'None' if it does not exist
    return second_largest
