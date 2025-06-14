
def remove_repeat_chars(s):
    # Create a dictionary to keep track of each character's frequency
    freq = {}

    # Loop through each character in the string
    for char in s:

        # If the character is not in the dictionary, add it and set its frequency to 1
        if char not in freq:
            freq[char] = 1

        # Otherwise, increment the character's frequency by 1
        else:
            freq[char] += 1

    # Create a new string with the characters that have a frequency of 1
    new_str = ""
    for char in s:
        if freq[char] == 1:
            new_str += char

    return new_str
