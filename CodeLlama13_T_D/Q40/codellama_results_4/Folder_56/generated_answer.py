
def return_n_smallest_chars(string):
    char_list = sorted(list(set(string)))
    n = 21
    if len(char_list) < n:
        raise ValueError("String must contain at least 21 unique characters")
    smallest_chars = []
    while len(smallest_chars) < n:
        smallest_chars.append(min(char_list))
        char_list.remove(min(char_list))
    return smallest_chars
