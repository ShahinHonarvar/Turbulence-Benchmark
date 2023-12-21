def return_n_greatest_chars(str1):
    greatest = str1[::-1]
    return ["".join(greatest[:i]) for i in range(1, len(greatest) + 1)]
