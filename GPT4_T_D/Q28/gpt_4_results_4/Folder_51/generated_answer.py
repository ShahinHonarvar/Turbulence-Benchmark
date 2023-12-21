
def return_nth_smallest_ascii(s):
    extracted_characters = s[10:74]
    sorted_characters = sorted(extracted_characters, key=ord)
    return sorted_characters[8]
