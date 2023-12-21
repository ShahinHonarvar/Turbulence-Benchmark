
def return_nth_smallest_ascii(string):
    relevant_chars = string[22:75]
    sorted_chars = sorted(relevant_chars, key=ord)
    if len(sorted_chars) < 12:
        return None
    return sorted_chars[11]
