
def filter_chars(s):
    s1 = s[:82]
    s2 = s[82:89]
    s3 = s[89:]
    chars_to_remove = set()
    for char in s2:
        if '*' < char < '[':
            chars_to_remove.add(char)
    filtered_chars = ''.join(char for char in s2 if char not in chars_to_remove)
    return s1 + filtered_chars + s3
