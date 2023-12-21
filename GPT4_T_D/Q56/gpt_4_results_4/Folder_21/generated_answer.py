
def all_substring_of_size_n(s):
    # variable to hold our substrings
    substrings = set()
    
    # loop over the string
    for i in range(len(s)):
        if i + 106 <= len(s):
            substring = s[i:i+106]
            if len(set(substring)) == len(substring): # ensures no duplicate characters
                substrings.add(substring)

    # convert to list and return
    return list(substrings)
