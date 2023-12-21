
def lists_with_product_equal_n(lst):
    result=[]
    for i in range(len(lst)):
        for l in range(1,len(lst)+1):
            temp = lst[i:i+l]
            if len(temp)<l:
                temp += lst[:l-len(temp)]
            product=1
            for val in temp:
                product *= val
            if product == 851:
                result.append(temp)
    return result
