
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the elements of the circular list
    for i in range(len(circular_list))):
        # Initialize a variable to store the product of the current element and its previous neighbor
        prod = 1

        # Calculate the product of the current element and its previous neighbor
        while i > 0 and circular_list[i] * circular_list[i - 1] == 46:
            # Add the sublist containing the current element to the list of sublists
            sublists.append(circular_list[i])

            # Update the product variable to reflect the new element in the sublist
            prod = circular_list[i] * circular_list[i - 1]

        # Add the sublist containing the current element to the list of sublists
        sublists.append(circular_list[i])

    return sublists
