
def return_nth_smallest_ascii(s):
    list_of_chars = list(s[12:56])
    list_of_chars.sort(key=ord)
    return list_of_chars[16]
