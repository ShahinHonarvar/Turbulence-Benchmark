
def lists_with_product_equal_n(circular_lst):
    circular_lst = circular_lst * 2
    result = []
    for size in range(1, len(circular_lst)//2 + 1):
        for i in range(len(circular_lst)//2):
            sublist = circular_lst[i:i+size]
            product = 1
            for num in sublist:
                product *= num
            if product == 74:
                result.append(sublist)
    return result
