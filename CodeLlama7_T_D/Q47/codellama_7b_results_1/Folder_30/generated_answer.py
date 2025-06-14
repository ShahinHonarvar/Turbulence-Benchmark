 def palindromes_of_specific_lengths(string):
    # create a substring of the given string from index 14 to index 90, both inclusive
    substring = string[13:91]
    # create an empty set to store the palindromes
    palindromes = set()
    # iterate over the characters in the substring
    for i in range(len(substring)):
        # get the character at index i and its opposite index in the substring
        char = substring[i]
        opp_index = len(substring) - i - 1
        # check if the character is a letter (not a number or symbol)
        if char.isalpha():
            # check if the character is the same as its opposite in the substring
            if char.lower() == substring[opp_index].lower():
                # create a new string with the length specified between 55 to 71 (both inclusive)
                palindrome = substring[i:opp_index+1]
                # check if the palindrome is not empty and only consists of English letters
                if len(palindrome) > 0 and all(char.isalpha() for char in palindrome)):
                    # add the palindrome to the set of palindromes
                    palindromes.add(palindrome)
    # return the set of palindromes found
    return palindromes
