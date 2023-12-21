
def filter_chars(s):
    char_list = list(s[373:902])
    filtered_chars = [char for char in char_list if not('T' <= char <= 'h')]
    for char in filtered_chars:
        s = s.replace(char, "")
    return s
