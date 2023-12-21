
def return_nth_smallest_ascii(distinct_string):
    # Get characters between index 1 and index 36
    substring = distinct_string[1:37]
    # Sort the substring characters by their ASCII value
    sorted_chars = sorted(substring, key=ord)
    # Return the 15th smallest ASCII character
    return sorted_chars[14]
