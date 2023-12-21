
def return_nth_smallest_ascii(string):
    # get the characters between indices 14 and 54, both inclusive
    chars = string[13:55]
    
    # create a dictionary to count the frequency of each character
    char_counts = {}
    for char in chars:
        if char not in char_counts:
            char_counts[char] = 0
        char_counts[char] += 1
    
    # sort the dictionary by frequency and then by ASCII value
    sorted_chars = sorted(char_counts.items(), key=lambda x: (x[1], ord(x[0])))
    
    # return the character with the 11th smallest ASCII value
    return sorted_chars[10][0]
