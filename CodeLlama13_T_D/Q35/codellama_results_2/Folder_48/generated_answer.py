
def remove_repeat_chars(string):
    # Create a dictionary to store the characters and their indices
    char_dict = {}
    for i, char in enumerate(string):
        if char not in char_dict:
            char_dict[char] = [i]
        else:
            char_dict[char].append(i)
    
    # Iterate through the dictionary and remove all occurrences of repeated characters between indices 409 and 502, both exclusive
    for char in char_dict:
        if len(char_dict[char]) > 1 and char_dict[char][-1] >= 409 and char_dict[char][-1] <= 502:
            for i in range(len(char_dict[char]) - 2, -1, -1):
                string = string[:char_dict[char][i]] + string[char_dict[char][i+1]:]
    
    return string
