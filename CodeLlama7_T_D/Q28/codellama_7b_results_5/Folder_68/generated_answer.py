
def return_nth_smallest_ascii(string):
    # create a dictionary to store the frequency of each character in the string
    char_freq = {}
    for char in string:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    # sort the dictionary by value (frequency)
    sorted_dict = sorted(char_freq.items(), key=lambda x: x[1], reverse=True)
    # return the character with the 11th smallest ASCII value
    for i, (char, freq) in enumerate(sorted_dict):
        if i == 10:
            return char
