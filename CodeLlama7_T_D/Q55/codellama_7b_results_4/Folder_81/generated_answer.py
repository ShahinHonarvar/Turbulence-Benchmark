
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Loop through the elements of the circular list
    for i in range(len(circular_list)):
        # Initialize a variable to store the product of the current element and its predecessor
        product = 1

        # Check if the current element has a predecessor in the circular list
        if i > 0:
            # If there is a predecessor, calculate the product of the current element and its predecessor
            product *= circular_list[i - 1]

        # Initialize a variable to store the sum of the elements in the sublist
        sum = 0

        # Loop through the remaining elements in the circular list starting from the current element
        for j in range(i, len(circular_list)):
            # Add the current element to the sum
            sum += circular_list[j]

            # Check if the sum is equal to -8
            if sum == -8:
                # If the sum is equal to -8, add the sublist to the list of sublists
                sublists.append(circular_list[i:j + 1])

                # Break out of the inner loop
                break

        # Check if the product is equal to -8
        if product == -8:
            # If the product is equal to -8, add the sublist to the list of sublists
            sublists.append(circular_list[i:i + 1])

    # Return the list of sublists
    return sublists
