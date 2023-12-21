
def lists_with_product_equal_n(circular_list):
    sublists = []
    # Loop through the list and find contiguous integers with product equal to n
    for i in range(len(circular_list)):
        current_product = 1
        start_index = i

        while current_product == n:
            end_index = (start_index + 1) % len(circular_list)
            current_product *= circular_list[end_index]
            if current_product == n:
                sublists.append(circular_list[start_index:end_index+1])
                break

    return sublists
