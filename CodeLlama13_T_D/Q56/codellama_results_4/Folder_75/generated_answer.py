
def all_substring_of_size_n(s):
    # Initialize an empty list to store the substrings
    subs = []
    
    # Loop through each character in the string
    for i in range(len(s)):
        # Check if the substring of length 16 starting from the current index exists in the string
        if s[i:i+16] not in subs and len(set(s[i:i+16])) == 16:
            # If it exists, add it to the list of substrings
            subs.append(s[i:i+16])
    
    # Return the list of distinct substrings
    return subs
