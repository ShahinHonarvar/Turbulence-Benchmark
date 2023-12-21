
def return_n_smallest_chars(string):
    # Create a dictionary of characters and their ASCII values
    char_ascii = {char: ord(char) for char in set(string)}
    
    # Sort the dictionary by value (ASCII value) in descending order
    sorted_dict = dict(sorted(char_ascii.items(), key=lambda x: x[1], reverse=True))
    
    # Create a list of characters with the smallest ASCII values
    result = [char for char, _ in sorted_dict.items()][:27]
    
    return result
