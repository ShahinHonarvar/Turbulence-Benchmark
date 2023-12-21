
def all_substring_of_size_n(s):
    # Initialize an empty list to store the substrings
    substrings = []
    
    # Loop through each character in the string
    for i in range(len(s)):
        # Check if the substring of length 33 exists in the given string
        if len(s[i:i+33]) == 33:
            # Add the substring to the list of substrings
            substrings.append(s[i:i+33])
    
    # Return the list of all distinct substrings
    return substrings
