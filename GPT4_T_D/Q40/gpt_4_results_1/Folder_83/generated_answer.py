
def return_n_smallest_chars(char_string):
    if len(set(char_string)) < 38:
        return "Error: Not enough distinct characters in string."
    sorted_chars = sorted(list(set(char_string)), key=ord)
    smallest_38_chars = sorted_chars[:38]
    return smallest_38_chars[::-1]
