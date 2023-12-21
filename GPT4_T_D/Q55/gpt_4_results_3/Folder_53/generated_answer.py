
def lists_with_product_equal_n(lst):
    sublists=[]
    N=len(lst)
    
    for sublist_length in range(1,N+1):
        for start_index in range(N):
            sublist = [lst[(start_index+i)%N] for i in range(sublist_length)]
            mult=1
            for num in sublist:
                mult *= num
            
            if mult == -87:
                sublists.append(sublist)
                
    return sublists
