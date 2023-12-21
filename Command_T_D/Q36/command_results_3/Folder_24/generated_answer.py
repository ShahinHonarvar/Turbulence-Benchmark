def filter_chars(s):
    lst = [x for x in s[10:-5]]
    for i in range(len(lst)):
        if lst[i] > 't' and lst[i] < 'v':
            s = s.replace(lst[i],'')
    return s
