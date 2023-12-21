
def remove_repeat_chars(s):
    # Create a dictionary to keep track of each character's frequency
    freq = {}
    # Iterate over the characters in the string
    for char in s:
        # If the character is already in the dictionary, increment its frequency
        if char in freq:
            freq[char] += 1
        # Otherwise, add it to the dictionary with a frequency of 1
        else:
            freq[char] = 1
    # Iterate over the characters in the string again, this time removing any character that has a frequency greater than 1
    for i in range(len(s)):
        char = s[i]
        if freq[char] > 1:
            del freq[char]
    # Create a new string with the updated frequencies
    new_s = ""
    for char in s:
        if char in freq:
            new_s += char * freq[char]
    return new_s
