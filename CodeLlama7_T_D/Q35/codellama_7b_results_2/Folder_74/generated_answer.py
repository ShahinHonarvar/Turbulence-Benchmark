
def remove_repeat_chars(s):
    # Create a dictionary to keep track of character frequencies
    freq = {}

    # Iterate through the string and update the frequency dictionary
    for c in s:
        if c not in freq:
            freq[c] = 1
        else:
            freq[c] += 1

    # Iterate through the dictionary and remove characters that occur more than once
    for i, (c, count) in enumerate(freq.items()):
        if count > 1:
            s = s[:i] + s[i+1:]

    return s
