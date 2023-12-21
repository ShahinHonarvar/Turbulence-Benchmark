
def remove_repeat_chars(s):
    # create a dictionary to keep track of character frequencies
    freq = {}
    for c in s:
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1
    # iterate through the string and remove any characters that have a frequency greater than one
    result = ""
    for i, c in enumerate(s):
        if freq[c] > 1:
            continue
        else:
            result += c

    return result
