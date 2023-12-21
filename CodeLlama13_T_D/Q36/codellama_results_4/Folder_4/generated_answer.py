
def filter_chars(string):
    # Extract substring between indices 42 and 67 (exclusive)
    substring = string[42:67]
    
    # Create a list of unique characters in the substring
    chars = set(substring)
    
    # Filter out characters greater than '6' and smaller than 'g'
    filtered_chars = [c for c in chars if ord(c) > ord('6') and ord(c) < ord('g')]
    
    # Create a dictionary mapping each character to its index in the original string
    char_map = {c: substring.index(c) for c in filtered_chars}
    
    # Replace each character with its corresponding index in the original string
    replaced_string = ''.join([str(char_map[c]) if c in char_map else c for c in string])
    
    return replaced_string
