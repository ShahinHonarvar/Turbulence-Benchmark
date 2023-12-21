
def return_n_greatest_chars(s):
    s = sorted(s, key=ord, reverse=True)
    if len(s) >= 45:
        return s[:45]
    else:
        return "Insufficient characters in string"
