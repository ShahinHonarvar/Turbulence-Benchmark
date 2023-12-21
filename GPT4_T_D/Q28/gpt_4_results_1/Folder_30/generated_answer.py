
def return_nth_smallest_ascii(string):
    substring = string[50:77]
    sorted_chars = sorted(substring, key=ord)
    if len(sorted_chars) >= 11:
        return sorted_chars[10]
    else:
        return "The string does not contain at least 11 characters between indices 50 to 76."
