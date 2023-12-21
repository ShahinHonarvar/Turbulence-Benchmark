
def lists_with_product_equal_n(lst):
    target = 96
    result = []
    size = len(lst)
    for n in range(1,sum([size-i for i in range(size)])+1):
        for i in range(size):
            part = lst[i:i+n]
            if len(part) < n:
                part = part + lst[0:n-len(part)]
            if len(part) == n:
                product = 1
                for num in part:
                    product *= num
                if product == target:
                    result.append(part)
    return result
