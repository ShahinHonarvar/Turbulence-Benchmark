
def return_n_smallest_chars(string):
    ascii_vals = [ord(char) for char in string]
    ascii_vals.sort()
    smallest_chars = []
    for val in ascii_vals[:56]:
        smallest_chars.append(chr(val))
    smallest_chars.sort(reverse=True)
    return smallest_chars
