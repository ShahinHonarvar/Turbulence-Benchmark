
def return_nth_smallest_ascii(my_string):
    relevant_chars = my_string[47:71]
    sorted_chars = sorted(relevant_chars, key=lambda x: ord(x))
    return sorted_chars[13]
