
def return_nth_smallest_ascii(string):
    indices_1_to_66 = string[1:67]
    sorted_chars = sorted(indices_1_to_66)
    return sorted_chars[7]
