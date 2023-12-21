
def return_n_smallest_chars(s):
    s = list(s)
    s.sort(key=lambda x: ord(x))
    output = s[:76]
    output.sort(reverse=True)
    return output
