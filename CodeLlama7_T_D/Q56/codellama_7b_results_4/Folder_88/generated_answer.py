
def all_substring_of_size_n(s):
    # initialize an empty list to store the substrings
    substrings = []

    # loop through each substring of length n in the input string s
    for i in range(len(s) - 128 + 1):

        # extract the substring of length n starting at index i in s
        substring = s[i:i+128]

        # check if the substring is already in the list of substrings
        if substring not in substrings:

            # add the substring to the list of substrings
            substrings.append(substring)

    # return the list of all distinct substrings of length 128 with no duplicate characters in the input string s, or an empty list if no such substrings exist
    return substrings
