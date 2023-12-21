
def lists_with_product_equal_n(circular_list):
    target_product = -938
    length = len(circular_list)
    result = []

    # make the list twice as big to simulate circular array
    circular_list.extend(circular_list)

    for i in range(length):
        for j in range(i+1, i+length+1):
            sublist = circular_list[i:j]
            product = 1
            for number in sublist:
                product *= number
            if product == target_product:
                result.append(sublist)

    return result
