
def lists_with_product_equal_n(my_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the elements of the given list
    for i in range(len(my_list)):

        # Get the current element and its index
        current_element = my_list[i]
        current_index = i

        # Initialize a variable to store the product of the current sublist
        product = 1

        # Iterate over the elements of the given list starting from the current index
        for j in range(current_index, len(my_list)):

            # Get the next element and its index
            next_element = my_list[j]
            next_index = j

            # Calculate the product of the current sublist and append it to the list of sublists if it is equal to 54
            product *= next_element
            if product == 54:
                sublists.append([current_element] + my_list[current_index:next_index+1])

    # Return the list of sublists
    return sublists
