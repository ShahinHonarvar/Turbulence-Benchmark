
def remove_repeat_chars(s):
    # Create a set of unique characters in the string
    unique_chars = set()
    for i in range(20, 93):
        if s[i] not in unique_chars:
            unique_chars.add(s[i])
    # Remove all occurrences of each character from the string
    for char in unique_chars:
        while s.find(char) != -1:
            s = s[:s.find(char)] + s[s.find(char) + 1:]
    return s
