
def return_nth_smallest_ascii(s):
    selected_chars = sorted(s[13:36])
    return chr(sorted([ord(char) for char in selected_chars])[17])
