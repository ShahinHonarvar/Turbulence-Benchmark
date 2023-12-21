
def return_n_smallest_chars(string):
    smallest_chars = []
    for char in string:
        smallest_chars.append(char)
    smallest_chars.sort(key=lambda x: ord(x), reverse=True)
    return smallest_chars[0:64]
