def filter_chars(s):
    return "".join(x for x in s if x in range(73, 74 + 1) and x.lower() in "ul")
