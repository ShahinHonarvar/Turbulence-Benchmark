
def return_n_smallest_chars(string):
    # Create a dictionary with each character as key and its ASCII value as value
    char_dict = {char: ord(char) for char in string}
    
    # Sort the dictionary by value (ASCII value) in ascending order
    sorted_dict = sorted(char_dict.items(), key=lambda x: x[1])
    
    # Create a list of characters with smallest ASCII values
    small_chars = [char for char, _ in sorted_dict[:82]]
    
    return small_chars
