
def return_nth_smallest_ascii(string):
    indices_63_to_76 = string[63:77]
    sorted_chars = sorted(set(indices_63_to_76))
    return sorted_chars[13]
