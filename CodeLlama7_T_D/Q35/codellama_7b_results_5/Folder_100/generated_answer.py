
def remove_repeat_chars(s):
    # Initialize a dictionary to keep track of characters
    char_count = {}

    # Iterate over the string and count the frequency of each character
    for c in s:
        if c not in char_count:
            char_count[c] = 1

        else:
            char_count[c] += 1

    # Remove all duplicate characters from the string
    for i in range(len(s)):
        c = s[i]

        if char_count[c] > 1:
            s = s[:i] + s[i+1:]

            char_count[c] -= 1

    return s
