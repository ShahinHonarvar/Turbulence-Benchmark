
def lists_with_product_equal_n(circular_list):
    circular_list += circular_list[0:len(circular_list)-1]
    result = []
    
    for i in range(len(circular_list)//2):
        for j in range(i+1, len(circular_list)):
            sublist = circular_list[i:j]
            product = 1
            for num in sublist:
                product *= num
            if product == 10: 
                result.append(sublist)
    return result
