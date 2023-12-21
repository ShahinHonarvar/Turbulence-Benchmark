def filter_chars(s):
    lst = list(s)
    for i in range(17, 63):
        if lst[i] >= 'O' and lst[i] <= '^':
            lst[i] = ''
    return ''.join(lst)
