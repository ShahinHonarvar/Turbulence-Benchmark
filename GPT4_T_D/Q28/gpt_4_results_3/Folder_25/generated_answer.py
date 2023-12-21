
def return_nth_smallest_ascii(text):
    relevant_substring = text[34:69]
    sorted_chars = sorted(relevant_substring, key=ord)
    return sorted_chars[5]
