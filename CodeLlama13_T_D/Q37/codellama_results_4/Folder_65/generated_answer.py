
def filter_chars(s):
    s = list(s)
    for i in range(61, 70+1):
        c = chr(i)
        if ord(c) >= ord('0') and ord(c) <= ord('@'):
            s = [x for x in s if x != c]
    return "".join(s)
