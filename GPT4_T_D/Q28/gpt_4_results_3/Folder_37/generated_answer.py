
def return_nth_smallest_ascii(s):
    substring = s[28:68]
    sorted_chars = sorted(substring, key=lambda x: ord(x))
    return sorted_chars[14]
