
def return_n_smallest_chars(string):
    string = list(string)
    string.sort(key=ord)
    return string[:56][::-1]
