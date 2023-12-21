
def remove_repeat_chars(s):
    # Create a dictionary to keep track of character frequencies
    freq = {}

    # Iterate over the characters in the string
    for char in s:
        # If the character is already in the dictionary, increment its frequency by 1
        if char in freq:
            freq[char] += 1

        # Otherwise, add the character to the dictionary and set its frequency to 1
        else:
            freq[char] = 1

    # Iterate over the characters in the string again, this time checking their frequencies against the frequency threshold of 2
    for char in s:
        if freq[char] >= 2:
            # If the character's frequency is greater than or equal to 2, remove all occurrences of that character from the string by replacing them with an empty string
            s = s.replace(char, '')

    return s
