
def lists_with_product_equal_n(circular_list):
    length = len(circular_list)
    result = []
    for start in range(length):
        for end in range(start + 1, start + length):
            sublist = circular_list[start:end] if end < length else circular_list[start:] + circular_list[:end - length]
            product = 1
            for number in sublist:
                product *= number
                if product > 76:
                    break
            if product == 76:
                result.append(sublist)
    return result
