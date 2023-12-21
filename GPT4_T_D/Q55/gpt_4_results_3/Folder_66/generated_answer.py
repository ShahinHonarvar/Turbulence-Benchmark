
def lists_with_product_equal_n(circular_list):
    target_product = 78
    size = len(circular_list)
    result = []
    for sublist_size in range(1, size + 1):
        for i in range(size):
            sublist = circular_list[i:i + sublist_size]
            if i + sublist_size > size:
                sublist.extend(circular_list[0:(i + sublist_size) % size])
            product = 1
            for n in sublist:
                product *= n
                if product == target_product:
                    result.append(sublist)
                    break
                elif product > target_product:
                    break
    return result
