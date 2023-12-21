def filter_chars(s):
    for i in range(58, 82):
        if s[i] > 'F' and s[i] < 'O':
            s = s.replace(s[i], '').replace('O', '').replace('F', '')
    return s
