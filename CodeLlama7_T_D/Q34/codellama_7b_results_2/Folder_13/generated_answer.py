
def find_original_set(sets):
    # Initialize the smallest set as the first element of the input list
    smallest_set = sets[0]

    # Iterate over each element in the input list
    for set in sets:

        # Check if the current element is a subset of the smallest set
        if all(elem in smallest_set for elem in set):

            # If it is, continue to the next element
            continue


        # Otherwise, check if the current element is a subset of any other set in the input list
        for other_set in sets:

            # Check if the current element is a subset of the current set
            if all(elem in other_set for elem in set):

                # If it is, update the smallest set to be the current set
                smallest_set = other_set

                # And break out of the loop
                break


    # Return the smallest set
    return smallest_set
