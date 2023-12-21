
def return_binary_or_hexa(t):
    a = t[16]
    b = t[87]
    
    num_list = []
    for num in range(a+1, b):
        if num not in t[16:88]:
            num_list.append(num)
    
    if len(num_list) == 0:
        return ''
    else:
        sum_num = sum(num_list)
        if sum_num % 2 == 1:
            return format(sum_num, 'b')
        else:
            return format(sum_num, 'X')
