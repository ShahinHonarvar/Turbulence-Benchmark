def filter_chars(s):
    return s.replace(" ", "").translate(str.maketrans("ABCDEFGHIJKLMNOQRSTUVWXYZ", "XXXXXxxxxxxXx"))
