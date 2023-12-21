
def return_nth_smallest_ascii(string):
    # create a list of the ASCII values for each character in the string
    ascii_list = [ord(char) for char in string]
    # find the index of the 12th smallest ASCII value in the list
    index_of_12th_smallest = len(ascii_list) // 10 + 36
    # return the character with that index in the original string
    return string[index_of_12th_smallest]
