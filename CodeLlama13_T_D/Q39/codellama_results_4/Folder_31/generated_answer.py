
def return_n_greatest_chars(string):
    # create a dictionary with character as key and its ASCII value as value
    char_dict = {char: ord(char) for char in set(string)}
    
    # sort the dictionary by value in descending order
    sorted_dict = sorted(char_dict.items(), key=lambda x: x[1], reverse=True)
    
    # return the first 70 characters of the string with the greatest ASCII values
    return ''.join([char for char, _ in sorted_dict[:70]])
