
def return_n_greatest_chars(string):
    # Create a dictionary with the character as the key and its ASCII value as the value
    char_dict = {char:ord(char) for char in string}
    # Sort the dictionary by the ASCII value of each character
    sorted_dict = sorted(char_dict.items(),key=lambda x:x[1],reverse=True)
    # Return the top 35 characters with the greatest ASCII values
    return [char for char,value in sorted_dict[:35]]
