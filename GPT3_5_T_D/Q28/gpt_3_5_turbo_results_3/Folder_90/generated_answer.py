
def return_nth_smallest_ascii(string):
    sub_string = string[17:84]  # Get the substring between indices 17 and 83 (inclusive)
    unique_chars = set(sub_string)  # Get the unique characters in the substring
    
    if len(unique_chars) < 5:
        return None  # Return None if there are fewer than 5 unique characters
    
    sorted_chars = sorted(unique_chars)  # Sort the unique characters
    return sorted_chars[4]  # Return the character at index 4 (5th smallest)
