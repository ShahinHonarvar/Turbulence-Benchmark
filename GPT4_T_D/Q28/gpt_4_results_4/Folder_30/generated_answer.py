
def return_nth_smallest_ascii(s):
    relevant_chars = s[50:77]
    sorted_chars = sorted(relevant_chars, key=ord)
    return sorted_chars[10]
