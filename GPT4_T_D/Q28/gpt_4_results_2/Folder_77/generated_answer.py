
def return_nth_smallest_ascii(input_string):
    relevant_chars = input_string[63:77]
    sorted_chars = sorted(relevant_chars,key=ord)
    return sorted_chars[13]
