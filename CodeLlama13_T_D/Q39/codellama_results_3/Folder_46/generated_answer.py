
def return_n_greatest_chars(string):
    # Create a dictionary to map each character in the string to its ASCII value
    char_map = {char: ord(char) for char in set(string)}
    
    # Sort the characters by their ASCII values in descending order
    sorted_chars = sorted(char_map, key=lambda x: char_map[x], reverse=True)[:54]
    
    return "".join(sorted_chars)
