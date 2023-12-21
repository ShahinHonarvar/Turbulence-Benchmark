 def remove_repeat_chars(s):
    # Create a dictionary to store the frequency of each character
    char_freq = {}
    for i in range(len(s)):
        if s[i] not in char_freq:
            char_freq[s[i]] = 1
        else:
            char_freq[s[i]] += 1
    # Create a list to store the characters that should be removed
    chars_to_remove = []
    for i in range(len(s)):
        if s[i] in char_freq and char_freq[s[i]] > 1:
            chars_to_remove.append(s[i])
    # Remove the characters from the string
    for c in sorted(chars_to_remove, reverse=True):
        s = s.replace(c, "")
    return s
