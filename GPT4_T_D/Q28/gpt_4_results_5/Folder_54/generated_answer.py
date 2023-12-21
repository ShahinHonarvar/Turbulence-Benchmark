
def return_nth_smallest_ascii(input_string):
    selected_chars = sorted(list(set(input_string[12:88])))
    return chr(sorted([ord(i) for i in selected_chars])[16])
