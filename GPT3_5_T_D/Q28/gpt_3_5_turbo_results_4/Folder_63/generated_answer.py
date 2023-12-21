
def return_nth_smallest_ascii(string):
    relevant_chars = string[47:71]
    relevant_chars = list(set(relevant_chars))
    relevant_chars.sort(key=lambda x: ord(x))
    return relevant_chars[13]
