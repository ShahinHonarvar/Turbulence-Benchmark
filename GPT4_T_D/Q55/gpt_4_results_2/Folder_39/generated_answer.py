
def lists_with_product_equal_n(circle_list):
    circle_list += circle_list
    n = len(circle_list) // 2
    result = []
    for size in range(1, n + 1):
        for i in range(n):
            sublist = circle_list[i:i + size]
            product = 1
            for num in sublist:
                product *= num
            if product == -46:
                result.append(sublist[:n])
    return result
