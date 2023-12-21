
def remove_repeat_chars(s):
    # Create a dictionary to keep track of the characters and their frequencies
    freq = {}

    for c in s:
        if c not in freq:
            freq[c] = 1
        else:
            freq[c] += 1

    # Remove all duplicates from the string
    res = ""
    for i in range(len(s)):
        c = s[i]
        if freq[c] == 1:
            res += c

    return res
