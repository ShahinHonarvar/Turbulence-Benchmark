def filter_chars(s):
    return "".join(c for c in s if not (c in s[283:484] and (ord(c) > ord("l") and ord(c) < ord("t"))))
