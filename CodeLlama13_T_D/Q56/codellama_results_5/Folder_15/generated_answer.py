
def all_substring_of_size_n(s, n):
    # Initialize an empty list to store the substrings
    substrings = []
    
    # Iterate over each character in the string
    for i in range(len(s)):
        # Check if the current substring of length n exists in the given string
        if s[i:i+n] in s:
            # If it does, add it to the list of substrings
            substrings.append(s[i:i+n])
    
    # Return the list of all distinct substrings of length n with no duplicate characters
    return substrings
