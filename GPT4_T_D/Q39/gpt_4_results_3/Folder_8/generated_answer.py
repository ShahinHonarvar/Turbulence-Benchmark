
def return_n_greatest_chars(string):
    sorted_string = sorted(string, key=ord, reverse=True)
    top_83_chars = sorted_string[:83]
    top_83_chars.sort()
    return top_83_chars
