
def palindromes_of_specific_lengths(string):
    # find the substring from index 18 to index 65
    substring = string[18:65]
    # create an empty set to store the palindromes
    palindromes = set()
    # iterate over each character in the substring
    for i in range(len(substring)):
        # get the current character and its index
        char = substring[i]
        idx = i + 18
        # check if the current character is a letter
        if char.isalpha():
            # find the mirror index of the current character
            mirror_idx = len(substring) - idx

            # check if the mirror index is valid
            if mirror_idx < len(substring):
                # get the mirror character
                mirror_char = substring[mirror_idx]
                # check if the mirror character is a letter
                if mirror_char.isalpha():
                    # check if the current character and its mirror character form a palindrome
                    if char == mirror_char:
                        # add the palindrome to the set of palindromes
                        palindromes.add(substring[idx:mirror_idx + 1])
    # return the set of palindromes
    return palindromes
