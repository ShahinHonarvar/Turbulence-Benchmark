def filter_chars(s):
    lst = list(range(51, 77))
    for i in range(51, 77):
        if s[i] >= 'V' and s[i] <= 'Y':
            lst.append(i)
    for i in range(len(s)):
        if s[i] >= 'V' and s[i] <= 'Y' and i in lst:
            lst.remove(i)
    s = ''.join(str(j) for j in range(len(s)) if j not in lst)
    return s
