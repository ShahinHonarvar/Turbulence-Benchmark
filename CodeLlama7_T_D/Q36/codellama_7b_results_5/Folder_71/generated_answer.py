
def filter_chars(s):
    # Create a new string with the same characters as s, but without any characters that are greater than '*' and smaller than '['
    filtered = ""
    for char in s:
        if char > "*" and char < "[":
            continue
        else:
            filtered += char
    return filtered
