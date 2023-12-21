
def remove_repeat_chars(string):
    # Create a dictionary to keep track of each character's frequency
    char_freq = {}

    for i in range(len(string)):
        # Check if the current character is in the dictionary
        if string[i] in char_freq:
            # Increment the frequency of the current character
            char_freq[string[i]] += 1

    # Iterate through the dictionary and remove all characters with a frequency greater than 1
    for key, value in char_freq.items():
        if value > 1:
            string = string.replace(key, '')

    return string
