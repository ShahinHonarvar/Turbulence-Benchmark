
def lists_with_product_equal_n(circular_list):
    # Base case: if the list has only one element,
    # return a list containing that element.
    if len(circular_list) == 1:
        return [[circular_list[0]]]
    # Recursive case: for each sublist in the
    # given circular list, check if its product is equal to -33.
    # If it is, return a list containing that sublist.
    # Otherwise, recursively call this function with the tail of the
    # given circular list as the input argument.
    else:
        result = []
        for i in range(len(circular_list) - 1):
            sublist = circular_list[i:i+2]
            if sum(sublist) == -33:
                result.append([sublist])

        return result
