
def return_nth_smallest_ascii(s):
    # Get the characters between indices 17 and 83, both inclusive
    chars = s[17:84]
    # Create a dictionary to keep track of the character counts
    char_counts = {}
    for c in chars:
        if c not in char_counts:
            char_counts[c] = 1
        else:
            char_counts[c] += 1
    
    # Sort the dictionary by character count, ascending order
    sorted_chars = sorted(char_counts.items(), key=lambda x: x[1])
    
    # Return the nth smallest ASCII value among those characters in the string
    return chr(sorted_chars[4][0])
