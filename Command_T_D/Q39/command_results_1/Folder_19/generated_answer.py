def return_n_greatest_chars(s):
    lst = list(s)
    return ''.join(sorted(lst, key=lambda x: x.lower()))[:58]
