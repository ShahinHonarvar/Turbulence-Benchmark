def return_n_smallest_chars(s):
    return [char for char in s if ord(char) < ord(s[0])]
