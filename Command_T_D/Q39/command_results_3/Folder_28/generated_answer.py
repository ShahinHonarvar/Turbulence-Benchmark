def return_n_greatest_chars(str1):
    return ["".join(sorted(str1, key=lambda x: ord(x), reverse=True)[:3])]
