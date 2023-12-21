
def return_nth_smallest_ascii(s):
    # Create a list of all characters in the string
    char_list = []
    for i in range(len(s)):
        if s[i].isalpha():
            char_list.append(s[i])
    # Sort the list of characters by ASCII value
    char_list.sort(key=ord)
    # Return the 19th smallest ASCII value
    return char_list[18]
