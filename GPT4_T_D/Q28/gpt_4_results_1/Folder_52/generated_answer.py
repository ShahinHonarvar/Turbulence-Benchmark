
def return_nth_smallest_ascii(s):
    relevant_chars = s[46:73]
    sorted_chars = sorted(relevant_chars, key=ord)
    return sorted_chars[14]
