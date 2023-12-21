
def return_binary_or_hexa(tup):
    if len(tup) < 33:
        return ''
    
    a = tup[19]
    b = tup[32]

    sum_numbers = sum(x for x in range(a + 1, b) if x not in tup[19: 33])

    if sum_numbers == 0:
        return ''

    if sum_numbers % 2 == 0:
        return format(sum_numbers, 'x')

    return format(sum_numbers, 'b')
