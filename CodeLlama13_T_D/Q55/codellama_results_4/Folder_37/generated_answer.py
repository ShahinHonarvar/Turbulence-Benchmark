
def lists_with_product_equal_n(circular_list, n):
    # Initialize an empty list to store the results
    result = []

    # Loop through each element in the circular list
    for i in range(len(circular_list)):
        # Initialize a variable to store the product of the elements
        product = 1

        # Loop through each element in the sublist
        for j in range(i, len(circular_list) + i):
            # Calculate the product of the elements
            product *= circular_list[j % len(circular_list)]

            # If the product is equal to n, add the sublist to the result list
            if product == n:
                result.append(circular_list[i:j])

    return result
