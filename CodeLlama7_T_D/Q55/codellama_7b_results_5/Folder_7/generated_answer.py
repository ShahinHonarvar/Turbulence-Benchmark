
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the elements of the circular list
    for i in range(len(circular_list)):

        # Initialize a variable to store the product of the current element and its predecessor
        product = 1

        # While the current element and its predecessor have a product equal to 537, add their indices to the sublists list
        while i > 0 and product == 537:
            sublists.append([i - 1, i])

            # Update the product variable by multiplying the current element and its predecessor
            product = circular_list[i - 1] * circular_list[i]

        # If the product is not equal to 537, break out of the loop
        if product != 537:
            break

    # Return the sublists list
    return sublists
