
def lists_with_product_equal_n(circular_list):
    res=[]
    for start in range(len(circular_list)):
        for end in range(start, start+len(circular_list)):
            sublist=circular_list[start:end % len(circular_list) + 1]
            product=1
            for num in sublist:
                product*=num
            if product==-23:
                res.append(sublist)
    return res
