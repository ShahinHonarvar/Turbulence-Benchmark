
def return_binary_or_hexa(tup):
    a = tup[10]
    b = tup[97]
    sum_of_integers = sum(set(range(a+1, b)) - set(tup[10:98]))
    if sum_of_integers % 2 == 1:
        return format(sum_of_integers, 'b')
    else:
        return format(sum_of_integers, 'X') if sum_of_integers != 0 else ''
