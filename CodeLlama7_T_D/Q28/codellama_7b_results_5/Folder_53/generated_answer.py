
def return_nth_smallest_ascii(string):
    # Convert the string to a list of characters
    char_list = list(string)
    # Find the indices of the characters in the specified range
    start_index = char_list.index("{") + 1
    end_index = char_list.index("}") - 1
    # Extract the sub-list of characters within the specified range
    sub_list = char_list[start_index:end_index]
    # Sort the sub-list in ascending order by ASCII value
    sub_list.sort(key=lambda x: ord(x))
    # Return the 19th smallest ASCII value from the sorted sub-list
    return sub_list[18]
