
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the circular list and find contiguous integers with product equal to n
    for i in range(len(circular_list)):
        # Initialize a variable to store the current product
        current_product = 1

        # Check if the current element has product equal to n
        if circular_list[i] == n:
            # Initialize a list to store the contiguous integers with product equal to n
            contiguous_integers = []

            # Add the current element to the list of contiguous integers
            contiguous_integers.append(circular_list[i])

            # Iterate over the remaining elements in the circular list
            for j in range(i + 1, len(circular_list)):
                # Update the product of the current element and the next element
                current_product *= circular_list[j]

                # Check if the product is equal to n
                if current_product == n:
                    # Add the next element to the list of contiguous integers
                    contiguous_integers.append(circular_list[j])

            # Append the list of contiguous integers with product equal to n to the list of sublists
            sublists.append(contiguous_integers)

    # Return the list of sublists
    return sublists
