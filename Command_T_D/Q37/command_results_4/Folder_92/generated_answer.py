def filter_chars(s):
    return "".join(i for i in s if i not in range(7, 'o' + 1))
