
def lists_with_product_equal_n(circle):
    result = []
    circle = circle + circle[:-1]  # Append the circle to itself to handle circularity

    for i in range(len(circle)):
        product = 1
        for j in range(i, len(circle)):
            product *= circle[j]
            if product == 33:
                result.append(circle[i: j + 1])
    return result
