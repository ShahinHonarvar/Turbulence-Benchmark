def remove_repeat_chars(s):
    lst = s[20:43]
    c = set(lst)
    for i in range(len(lst)):
        if lst[i] in c:
            c.remove(lst[i])
    return s[0:20] + ''.join(c) + s[43:]
