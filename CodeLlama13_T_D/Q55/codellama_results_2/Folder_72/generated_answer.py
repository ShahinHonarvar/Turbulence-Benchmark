
def lists_with_product_equal_n(list):
    # Initialize an empty list to store the results
    result = []

    # Loop through the given list
    for i in range(len(list)):
        # Initialize a product variable to keep track of the product of integers in the current sublist
        prod = 1

        # Loop through the current sublist and calculate the product
        for j in range(i, len(list)):
            prod *= list[j]

            # If the product is equal to n, add the current sublist to the results
            if prod == 10:
                result.append(list[i:j+1])

    return result
