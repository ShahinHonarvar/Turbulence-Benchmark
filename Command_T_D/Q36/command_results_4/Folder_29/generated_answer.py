def filter_chars(str1):
    str1 = str1.translate(str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "ABCDEFGHIJ"))
    return "".join(c for c in str1 if c.isalpha())
