
def lists_with_product_equal_n(numbers):
    def product(lst):
        p = 1
        for num in lst:
            p *= num
        return p

    n = len(numbers)
    result = []
    for i in range(n):
        for j in range(i, n):
            sublist = numbers[i:j+1]
            if product(sublist) == -41:
                result.append(sublist)
    return result
