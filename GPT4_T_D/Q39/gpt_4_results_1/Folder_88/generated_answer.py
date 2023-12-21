
def return_n_greatest_chars(s):
    asc_values = list(s)
    asc_values.sort(key=ord, reverse=True)
    return sorted(asc_values[:84])
