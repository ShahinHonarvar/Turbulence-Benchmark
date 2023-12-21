
def return_n_greatest_chars(s):
    sorted_string = sorted(s, reverse=True)[:11]
    sorted_string.sort()
    return sorted_string
