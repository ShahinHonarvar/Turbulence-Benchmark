
def return_nth_smallest_ascii(str):
    relevant_chars = list(str[34:82])
    relevant_chars.sort(key=ord)
    return relevant_chars[11]
