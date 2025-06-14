
def remove_repeat_chars(s):
    # Create a dictionary to keep track of character frequencies
    freq = {}

    # Loop through each character in the string and update the frequency count
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    # Remove all characters with a frequency greater than 1 between indices 46 and 91
    for i in range(46, 91):
        if s[i] in freq and freq[s[i]] > 1:
            j = i + 1

            # Loop through each character after the current one and update their indices accordingly
            while j < len(s):
                if s[j] == s[i]:
                    freq[s[i]] -= 1

                    # If there are no more occurrences of the current character, remove it from the string
                    if freq[s[i]] == 0:
                        s = s[:i] + s[i+1:]

                j += 1

    return s
