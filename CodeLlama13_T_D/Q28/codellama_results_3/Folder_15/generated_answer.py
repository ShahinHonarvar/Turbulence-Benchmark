
def return_nth_smallest_ascii(string):
    # Initialize a dictionary to store the count of each character
    char_count = {}
    for char in string:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    
    # Sort the dictionary by the value (i.e., count) in descending order
    sorted_chars = sorted(char_count.items(), key=lambda x: x[1], reverse=True)
    
    # Return the character with the 6th smallest ASCII value among those characters that occur between indices 0 to 5, both inclusive
    return sorted_chars[5][0]
