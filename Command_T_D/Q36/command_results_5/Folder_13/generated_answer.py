def filter_chars(s):
    lst = list(range(323, 527))
    for i in range(323, 526):
        if s[i] > ')' and s[i] < 'O':
            lst.remove(i)
    return ''.join(str(c) for c in s if c in lst)
