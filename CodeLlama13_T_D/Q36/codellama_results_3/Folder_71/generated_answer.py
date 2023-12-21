
def filter_chars(s):
    s = list(s)
    for i in range(82, 89):
        if s[i] > '*' and s[i] < '[':
            s = [x for x in s if x != s[i]]
    return "".join(s)
