
def filter_chars(s):
    # Create a new string with all occurrences of characters between indices 42 and 97, both inclusive, removed
    filtered_string = ""
    for i in range(len(s)):
        if not (42 <= i < 98) or s[i] < "*" or s[i] > "b":
            filtered_string += s[i]
    return filtered_string
