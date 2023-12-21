
def return_n_greatest_chars(s):
    sorted_s = sorted(set(s), key=ord, reverse=True)
    return sorted(sorted_s[:57])
