
def return_nth_smallest_ascii(string):
    # Get the characters between indices 40 and 60, both inclusive
    chars = string[39:61]
    
    # Create a dictionary to count the frequency of each character
    char_counts = {}
    for char in chars:
        if char not in char_counts:
            char_counts[char] = 0
        char_counts[char] += 1
    
    # Sort the characters by their ASCII value and return the 19th smallest character
    sorted_chars = sorted(char_counts, key=lambda x: ord(x))
    return sorted_chars[18]
