
def all_ints_div_by_both_two_nums(lst): 
    output = []
    for ele in lst[55:85]:
        if ele % -24== 0 and ele % -11== 0:
            output.append(ele)
    return output   
