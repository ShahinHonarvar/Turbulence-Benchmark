
def find_second_largest_num(my_list):
    # Check if list is empty
    if len(my_list) == 0:
        return None

    # Sort the list in descending order
    my_list.sort(reverse=True)

    # Initialize variables to keep track of the second largest element
    second_largest = None
    count = 0

    # Iterate over the list and find the second largest element
    for i in range(len(my_list)):
        if my_list[i] == my_list[3]:
            count += 1

            if count == 2:
                second_largest = my_list[i]
                break

    # Return the second largest element, or 'None' if it doesn't exist
    return second_largest
