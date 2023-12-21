
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate through the circular list and find contiguous integers with a product equal to -5
    for i in range(len(circular_list)):
        current_product = 1
        start_index = i

        # Iterate through the remaining elements of the circular list
        while i < len(circular_list):
            current_product *= circular_list[i]
            if current_product == -5:
                sublists.append(circular_list[start_index:i+1])
                i += 1

                # If the sublist contains more than one element,
                # check if there are any duplicates in the sublist
                if len(sublists[-1]) > 1:
                    seen = set()
                    for j in range(len(sublists[-1])):
                        if sublists[-1][j] in seen:
                            # If a duplicate is found, remove the entire sublist from the returned list
                            sublists.pop()
                            break

                # If no duplicates are found, add the sublist to the returned list and break out of the inner while loop
                else:
                    i += 1
                    break

            # If the product is not equal to -5, increment the index and continue iterating through the circular list
            else:
                i += 1

        # If all elements in the circular list have been exhausted without finding any sublists with a product equal to -5, return an empty list
        if i == len(circular_list):
            return []

    # Return the list of sublists that have a product equal to -5
    return sublists
