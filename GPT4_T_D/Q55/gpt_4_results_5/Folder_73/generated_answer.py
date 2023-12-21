
def lists_with_product_equal_n(circle):
    n = len(circle)
    circle_double = circle * 2
    results = []
    for i in range(n):
        for j in range(i+1, i+n+1):
            sub_list = circle_double[i:j]
            product = 1
            for num in sub_list:
                product *= num
            if product == 40:
                results.append(sub_list)
    return results
