
def lists_with_product_equal_n(circle):
    circle += circle
    result = []
    for i in range(len(circle)):
        for j in range(i+1, len(circle)):
            sublist = circle[i:j]
            product = 1
            for num in sublist:
                product *= num
            if product == -779:
                result.append(sublist)
    unique_results = []
    [unique_results.append(result) for result in result if result not in unique_results]
    return unique_results
