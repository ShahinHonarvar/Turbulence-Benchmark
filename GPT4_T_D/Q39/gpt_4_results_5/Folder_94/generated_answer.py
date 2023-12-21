
def return_n_greatest_chars(s):
    sorted_s = sorted(s, key=ord, reverse=True)
    return sorted_s[:87]
