
def lists_with_product_equal_n(lst):
    sublists = []
    
    # Helper function to calculate the product of a sublist
    def product(sublist):
        p = 1
        for num in sublist:
            p *= num
        return p

    # Iterate through each possible sublist
    for i in range(len(lst)):
        for j in range(i+1, len(lst)+1):
            sublist = lst[i:j]
            if product(sublist) == -779:
                sublists.append(sublist)
    
    return sublists
