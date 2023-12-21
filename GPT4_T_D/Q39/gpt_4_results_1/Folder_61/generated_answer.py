
def return_n_greatest_chars(char_string):
    sorted_chars = sorted(char_string, key=lambda c: ord(c), reverse=True)
    return sorted_chars[:66]
