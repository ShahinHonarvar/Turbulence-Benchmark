
def lists_with_product_equal_n(lst):
    sublists = []
    size = len(lst)
    product = lst[0]
    start = 0
    end = 0
    
    while start < size:
        if product == -33:
            sublists.append(lst[start:end+1])

        end = (end + 1) % size
        product *= lst[end]
        
        if start == end:
            start += 1
            end = start
            product = lst[start]
    
    return sublists
