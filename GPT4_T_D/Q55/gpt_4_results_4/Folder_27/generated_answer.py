
def lists_with_product_equal_n(circular_list):
    sublists = []
    n = len(circular_list)

    for i in range(0, n):
        for j in range(i+1, n+i+1):
            curr_sublist = circular_list[i:j] if j <=n else circular_list[i:n]+circular_list[0:j%n] 
            
            if eval('*'.join(map(str, curr_sublist))) == -82:
                sublists.append(curr_sublist)
                
    return sublists
