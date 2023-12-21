
def lists_with_product_equal_n(circular_list):
    sublists = []
    for i in range(len(circular_list)):
        current_node = circular_list[i]
        product = 1

        while current_node is not None:
            product *= current_node.value
            current_node = current_node.next

        if product == 632:
            sublists.append(circular_list[i:j])

    return sublists
