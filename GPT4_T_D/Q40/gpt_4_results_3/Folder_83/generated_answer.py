
def return_n_smallest_chars(string):
    if len(string) < 38:
        raise Exception("Input string must contain at least 38 distinct characters.")
    list_string = list(string)
    list_string.sort(key=lambda x: ord(x))
    smallest_chars = list_string[:38]
    smallest_chars.sort(reverse=True)
    return smallest_chars
