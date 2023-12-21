
def all_substring_of_size_n(s):
    # initialize an empty list to store the substrings
    substrings = []
    
    # loop through each character in the string
    for i in range(len(s)):
        # check if the substring starting from this index has length equal to 24
        if len(s[i:i+24]) == 24:
            # add the substring to the list of substrings
            substrings.append(s[i:i+24])
    
    # return the list of distinct substrings
    return list(set(substrings))
