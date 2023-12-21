
def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    circular_list = circular_list + circular_list
    results = []
    
    for size in range(1, n+1):
        for i in range(n):
            sublist = circular_list[i:i+size]
            product = 1
            for num in sublist:
                product *= num
            if product == 27:
                results.append(sublist)
    return results
