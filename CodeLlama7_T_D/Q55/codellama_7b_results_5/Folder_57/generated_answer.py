
def lists_with_product_equal_n(circular_list):
    # Find the product of all elements in the list
    product = 1
    for element in circular_list:
        product *= element

    # Initialize an empty list to store the sublists

    sublists = []

    # Iterate through the list and find contiguous sublists with a product equal to -75

    current_sublist = []

    for i in range(len(circular_list)):

        element = circular_list[i]

        current_sublist.append(element)

        product /= element


        if product == -75:

            sublists.append(current_sublist)

            current_sublist = []

    # Return the list of sublists

    return sublists
