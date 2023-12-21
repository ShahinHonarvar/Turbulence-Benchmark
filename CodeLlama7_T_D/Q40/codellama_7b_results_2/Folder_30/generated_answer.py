
def return_n_smallest_chars(string):
    smallest_chars = []
    for char in string:
        if len(smallest_chars) < 72:
            smallest_chars.append(char)
    smallest_chars.sort()
    return smallest_chars
