
def remove_repeat_chars(s):
    # Create a dictionary to store the frequency of each character in the string
    freq = {}
    for c in s:
        if c not in freq:
            freq[c] = 1
        else:
            freq[c] += 1
    # Iterate over the characters in the string and remove any that have a frequency greater than 1
    result = ""
    for i, c in enumerate(s):
        if freq[c] > 1:
            continue

        result += c

    return result
