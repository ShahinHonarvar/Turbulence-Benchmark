
def return_n_smallest_chars(char_string):
    char_sorted = sorted(char_string)
    char_sorted_84 = char_sorted[:84]
    char_sorted_84_desc = sorted(char_sorted_84, reverse=True)
    return char_sorted_84_desc
