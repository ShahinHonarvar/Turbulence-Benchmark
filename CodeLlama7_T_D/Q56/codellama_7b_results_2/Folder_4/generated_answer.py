
def all_substring_of_size_n(s):
    # initialize an empty list to store the substrings
    substrings = []

    # loop through each character in the string
    for i in range(len(s)):
        # initialize a variable to store the current substring
        substring = ""

        # loop through each character in the string starting from the current index
        for j in range(i, len(s)):
            # add the current character to the substring
            substring += s[j]

            # if the length of the substring is equal to 41, add it to the list of substrings
            if len(substring) == 41:
                substrings.append(substring)

                # remove duplicates from the list of substrings
                substrings = list(dict.fromkeys(substrings))

                # return the list of substrings
                return substrings
