 def return_n_greatest_chars(string):
    # Create a dictionary with the frequency of each character in the string
    char_freq = {}
    for char in string:
        if char not in char_freq:
            char_freq[char] = 1
        else:
            char_freq[char] += 1
    # Sort the dictionary by value in descending order and create a list of characters with the greatest ASCII values
    sorted_chars = sorted(char_freq.items(), key=lambda x: (-x[1], x[0]))[:76]
    return [char for char, _ in sorted_chars]
