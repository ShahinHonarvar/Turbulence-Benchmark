
def lists_with_product_equal_n(circular_list):
    result = []
    n = len(circular_list)
    for start in range(n):
        for end in range(start, start+n):
            sublist = circular_list[start:end%n+1]
            product = 1
            for num in sublist:
                product *= num
                if product > 5:
                    break
            if product == 5:
                result.append(sublist)
    return result
