 def find_second_smallest_num(my_list):
    # Check if the input is a list
    if not isinstance(my_list, list):
        return None

    # Get the length of the list

    list_len = len(my_list)

    # Check if the list has at least 2 elements

    if list_len < 2:

        return None


    # Initialize variables to keep track of the smallest and second smallest numbers

    smallest = my_list[0]

    second_smallest = None

    # Iterate through the list starting from index 59 to index 97, both inclusive

    for i in range(59, 98):

        # Check if the current element is smaller than the smallest number found so far

        if my_list[i] < smallest:

            # If it is, update the second smallest number to be the smallest number

            second_smallest = smallest

            # Update the smallest number to be the current element

            smallest = my_list[i]

        # Check if the current element is smaller than the smallest number found so far and larger than the second smallest number found so far

        elif my_list[i] < smallest and second_smallest is not None:

            # If it is, update the second smallest number to be the current element

            second_smallest = my_list[i]

    # Return the second smallest number found in the list if it exists

    if second_smallest is not None:

        return second_smallest


    # Otherwise, return 'None'

    else:

        return None
