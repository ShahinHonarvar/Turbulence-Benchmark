
def return_n_smallest_chars(string):
    char_list = []
    for i in range(26):
        char_list.append(chr(i + 97)) # add the character with ascii value i to the list
    
    sorted_char_list = sorted(char_list, key=lambda x: ord(x), reverse=True) # sort the list in descending order based on ASCII values
    
    return [char for char in string if char in sorted_char_list] # return the list of characters from the given string that are in the sorted list
