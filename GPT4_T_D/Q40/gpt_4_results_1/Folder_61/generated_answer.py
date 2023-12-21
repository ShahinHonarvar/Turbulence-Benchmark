
def return_n_smallest_chars(s):
    if len(s) < 66:
        return "The input string must contain at least 66 distinct characters."
    else:
        char_list = sorted(list(s))
        smallest_66_char = char_list[:66]
        smallest_66_char.sort(reverse=True)
        return smallest_66_char
