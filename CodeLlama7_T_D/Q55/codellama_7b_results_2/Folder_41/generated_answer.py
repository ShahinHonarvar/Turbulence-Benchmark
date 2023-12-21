
def lists_with_product_equal_n(circular_list):
    result = []
    # Iterate over the circular list and find all sublists with product equal to -20
    for i in range(len(circular_list)):
        product = 1

        for j in range(i, len(circular_list)):
            product *= circular_list[j]

            if product == -20:
                result.append(circular_list[i:j+1])

    return result
