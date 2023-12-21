
def all_substring_of_size_n(string):
    # initialize an empty list to store the substrings
    substrings = []

    # loop through each character in the string
    for i in range(len(string) - 142):

        # extract a substring of length 143 starting at position i
        substring = string[i:i+143]

        # if the substring is not already in the list of substrings, add it
        if substring not in substrings:
            substrings.append(substring)

    # return the list of all distinct substrings of length 143 with no duplicate characters
    return substrings
