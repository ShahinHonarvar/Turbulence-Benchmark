
def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        for j in range(i+1, n+1):
            temp_list = lst[i:j] if i == j-1 else lst[i:j] + lst[0:i]
            product = 1
            for num in temp_list:
                product *= num
            if product == 32:
                result.append(temp_list)
    return result
