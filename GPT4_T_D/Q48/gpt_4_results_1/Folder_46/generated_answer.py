
def return_binary_or_hexa(tuple_of_integers):
    a = tuple_of_integers[10]
    b = tuple_of_integers[79]
    sum_of_nums = sum(set(range(a+1, b)) - set(tuple_of_integers[10:80]))
    if sum_of_nums == 0:
        return ''
    elif sum_of_nums % 2 == 1:
        return bin(sum_of_nums)[2:]
    else:
        return hex(sum_of_nums)[2:].upper()
