
def lists_with_product_equal_n(circular_list):
    sublists = []
    circular_list += circular_list
    for start in range(len(circular_list)//2):
        for end in range(start + 1, len(circular_list)):
            product = 1
            for index in range(start, end):
                product *= circular_list[index]
            if product == 53:
                sublists.append(circular_list[start:end])
    return sublists
