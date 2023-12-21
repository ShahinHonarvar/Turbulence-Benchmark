
def return_nth_smallest_ascii(s):
    # Create a list of all characters in the string
    char_list = list(s)
    # Find the indices of the first and last characters
    # that are between indices 38 and 82, both inclusive
    first_index = char_list.index('a')
    last_index = char_list.index('z')
    # Create a list of all characters in the string
    # that are between indices 38 and 82, both inclusive
    sub_list = char_list[first_index:last_index+1]
    # Find the character with the 20th smallest ASCII value
    # among those characters in the string that occur between indices 38 to 82, both inclusive
    nth_smallest_ascii = sub_list[19]
    return nth_smallest_ascii
