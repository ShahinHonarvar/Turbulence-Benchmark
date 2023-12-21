
def lists_with_product_equal_n(lst):
    def product(lst):
        result = 1
        for num in lst:
            result *= num
        return result
    
    sublists = []
    length = len(lst)
    for i in range(length):
        for j in range(i, length):
            temp = lst[i:j+1] + lst[0:i] + lst[j+1:length]
            if product(temp) == -97:
                sublists.append(temp)
    
    return sublists
