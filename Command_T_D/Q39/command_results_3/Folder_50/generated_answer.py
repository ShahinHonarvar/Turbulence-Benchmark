def return_n_greatest_chars(s):
    return ["".join(sorted(s, key=lambda x: ord(x), reverse=True)) for i in range(16)]
