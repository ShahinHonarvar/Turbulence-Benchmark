
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Loop through each element in the circular list
    for i in range(len(circular_list)):

        # Calculate the product of all elements up to and including the current element
        product = 1
        for j in range(i + 1):
            product *= circular_list[j]

        # If the product is equal to n, add the sublist containing the current element to the list of sublists
        if product == n:
            sublists.append([circular_list[i]])

    # Return the list of sublists
    return sublists
