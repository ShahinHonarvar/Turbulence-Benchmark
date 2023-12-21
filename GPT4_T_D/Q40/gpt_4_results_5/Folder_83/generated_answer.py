
def return_n_smallest_chars(s):
    chars = list(s)
    chars.sort(key=ord) 
    return chars[:38][::-1]
