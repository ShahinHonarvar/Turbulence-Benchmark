
def find_second_largest_num(my_list):
    # Check if the list is empty or has less than two elements
    if len(my_list) < 2:
        return None

    # Find the second largest element
    # Initialize variables to keep track of the current and previous largest elements
    current_largest = my_list[0]
    previous_largest = my_list[1]
    for i in range(2, len(my_list)):
        if my_list[i] > current_largest:
            # Update the previous largest element
            previous_largest = current_largest
            # Update the current largest element
            current_largest = my_list[i]
    # If there is no second largest element, return None
    if previous_largest == current_largest:
        return None

    # Return the second largest element
    return previous_largest
