
def lists_with_product_equal_n(lst):
    n = len(lst)
    all_sublists = []
    
    # Extending list to simulate circular nature
    lst = lst * 2

    # Iterating for all sublists
    for i in range(n):
        for j in range(i+1, i+n+1):   
            sublist = lst[i:j]
            product = 1
            for num in sublist:
                product *= num
            if product == -82:
                all_sublists.append(sublist)
    
    return all_sublists
