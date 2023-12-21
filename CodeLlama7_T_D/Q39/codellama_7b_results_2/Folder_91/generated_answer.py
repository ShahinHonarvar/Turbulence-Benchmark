
def return_n_greatest_chars(string, n=6):
    if len(string) < n:
        raise ValueError("Length of string is less than n")
    char_list = []
    for char in string:
        char_list.append((ord(char), char))
    char_list = sorted(char_list, reverse=True)[:n]
    return [char for ord_, char in char_list]
