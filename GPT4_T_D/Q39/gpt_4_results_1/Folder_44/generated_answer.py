
def return_n_greatest_chars(s):
    asc_values = sorted(s, key=ord, reverse=True)[:73]
    return sorted(asc_values)
