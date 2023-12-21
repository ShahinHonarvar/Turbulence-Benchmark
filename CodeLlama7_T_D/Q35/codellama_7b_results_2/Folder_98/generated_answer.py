
def remove_repeat_chars(s):
    # create a dictionary to keep track of character frequencies
    freq = {}

    for i in range(len(s)):
        if s[i] not in freq:
            freq[s[i]] = 1

        else:

            freq[s[i]] += 1

    # create a new string with the characters removed
    # that occur more than once between indices 0 and 7
    new_str = ""

    for i in range(len(s)):
        if s[i] not in freq or freq[s[i]] <= 1:
            new_str += s[i]

    return new_str
