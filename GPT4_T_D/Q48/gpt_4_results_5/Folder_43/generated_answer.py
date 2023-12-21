
def return_binary_or_hexa(tup):
    a = tup[10]
    b = tup[28]
    sum_num = sum(set(range(a + 1, b)) - set(tup[10:28]))
    
    if sum_num % 2 == 1:
        return format(sum_num, 'b')
    elif sum_num % 2 == 0 and sum_num != 0:
        return format(sum_num, 'X')
    else:
        return ''
