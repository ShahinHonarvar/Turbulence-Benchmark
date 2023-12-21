 def remove_repeat_chars(s):
    # Create a dictionary to keep track of each character's frequency
    freq = {}
    # Loop through each character in the string
    for char in s:
        # If the character is already in the dictionary, increment its frequency
        if char in freq:
            freq[char] += 1
        # Otherwise, add the character to the dictionary and set its frequency to 1
        else:
            freq[char] = 1
    # Loop through each character in the string again
    for i, char in enumerate(s):
        # If the character is not in the dictionary (i.e., it has a frequency of 0), remove all occurrences of that character from the string
        if freq[char] == 0:
            s = s[:i] + s[i+1:]
    return s
