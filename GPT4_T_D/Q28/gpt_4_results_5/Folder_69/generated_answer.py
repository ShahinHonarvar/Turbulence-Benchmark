
def return_nth_smallest_ascii(string):
    extracted_chars = string[67:78]
    sorted_chars = sorted(extracted_chars, key=ord)
    return sorted_chars[6]
