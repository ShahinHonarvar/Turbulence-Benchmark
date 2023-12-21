
def return_binary_or_hexa(my_tuple):
    a = my_tuple[22]
    b = my_tuple[24]
    absence = [i for i in range(a+1, b) if i not in my_tuple[22:25]]
    if absence:
        my_sum = sum(absence)
        if my_sum % 2 == 0:
            return format(my_sum, 'X')
        else:
            return format(my_sum, 'b')
    else:
        return ''
