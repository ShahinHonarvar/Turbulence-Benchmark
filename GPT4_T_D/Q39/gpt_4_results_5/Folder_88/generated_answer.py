
def return_n_greatest_chars(s):
    sorted_string = sorted(s, key=ord, reverse=True)[:84]
    sorted_string.sort()
    return sorted_string
