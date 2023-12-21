
def return_nth_smallest_ascii(s):
    relevant_chars = s[35:53]
    sorted_chars = sorted(relevant_chars, key=ord)
    return sorted_chars[9]
