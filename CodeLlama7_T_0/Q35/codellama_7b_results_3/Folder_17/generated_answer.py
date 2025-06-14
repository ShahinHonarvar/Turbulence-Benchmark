
def remove_repeat_chars(s):
    # Create a dictionary to keep track of character frequencies
    freq = {}
    for c in s:
        if c not in freq:
            freq[c] = 1
        else:
            freq[c] += 1
    # Iterate over the string and remove characters that occur more than once
    result = ""
    for i, c in enumerate(s):
        if freq[c] > 1:
            continue
        else:
            result += c

    return result
