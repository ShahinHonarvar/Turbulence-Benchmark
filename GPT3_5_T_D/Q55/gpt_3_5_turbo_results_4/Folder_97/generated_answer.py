
def lists_with_product_equal_n(lst):
    n = len(lst)
    output = []
    
    def find_sublists(start_idx):
        product = 1
        sub_list = []
        
        for i in range(start_idx, start_idx+n):
            idx = i % n
            product *= lst[idx]
            sub_list.append(lst[idx])
            
            if product == -938:
                output.append(sub_list[:])
            elif product > 0:
                break
    
    for i in range(n):
        find_sublists(i)
    
    return output
