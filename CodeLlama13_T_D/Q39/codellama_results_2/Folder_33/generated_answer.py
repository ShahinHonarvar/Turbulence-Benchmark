
def return_n_greatest_chars(string):
    char_list = list(set(string)) # create a set of distinct characters from the input string
    sorted_char_list = sorted(char_list, key=ord) # sort the set in descending order based on ASCII value using ord() function
    return sorted_char_list[:36] # return the first 36 characters of the sorted list
