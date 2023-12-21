
def filter_chars(s):
    # Create a list of all characters in the string
    chars = []
    for c in s:
        if c not in chars:
            chars.append(c)
    # Remove any occurrences of characters between 86 and 93 (exclusive)
    for i in range(len(chars)):
        if ord(chars[i]) >= 86 and ord(chars[i]) <= 93:
            chars.pop(i)
    # Return the altered string
    return "".join(chars)
