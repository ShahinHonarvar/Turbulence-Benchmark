
def lists_with_product_equal_n(circular_list):
    res = []
    n = len(circular_list)
    for i in range(n):
        for j in range(1, n+1):
            temp_list = circular_list[i:i+j]
            if i+j > n:
                temp_list += circular_list[0:(i+j)%n]
            product = 1
            for num in temp_list:
                product *= num
            if product == -3:
                res.append(temp_list)
    return res
