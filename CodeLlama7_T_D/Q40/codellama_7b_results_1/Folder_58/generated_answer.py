
def return_n_smallest_chars(string):
    smallest_chars = []
    for char in string:
        smallest_chars.append(char)
    smallest_chars.sort(reverse=True)
    return smallest_chars[:49]
