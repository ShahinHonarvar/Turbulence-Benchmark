
def return_n_smallest_chars(string):
    # Create a dictionary with each character as key and its ASCII value as value
    char_ascii = {char: ord(char) for char in string}
    
    # Sort the dictionary by value in descending order
    sorted_chars = sorted(char_ascii.items(), key=lambda x: x[1], reverse=True)
    
    # Return a list of exactly 35 characters with the smallest ASCII values
    return [char for char, _ in sorted_chars[:35]]
