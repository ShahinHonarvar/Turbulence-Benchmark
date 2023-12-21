
def return_nth_smallest_ascii(s):
    # Convert string to a list of characters
    char_list = list(s)
    # Find the indices of the characters between 30 and 70 (inclusive)
    start_index = char_list.index('@')
    end_index = char_list.index('~') - 1
    # Extract the characters from the list that are within the specified range
    sub_list = char_list[start_index:end_index]
    # Sort the list in ascending order by ASCII value
    sorted_sub_list = sorted(sub_list, key=lambda x: ord(x))
    # Return the character with the 15th smallest ASCII value
    return sorted_sub_list[14]
