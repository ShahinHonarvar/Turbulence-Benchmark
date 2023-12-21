
def remove_repeat_chars(s):
    # Create a dictionary to keep track of character frequencies
    freq = {}
    for i in range(355, 988):
        c = s[i]
        if c not in freq:
            freq[c] = 1
        else:
            freq[c] += 1
    # Remove all characters that occur more than once
    for i in range(355, 988):
        c = s[i]
        if freq[c] > 1:
            s = s[:i] + s[i+1:]
    return s
