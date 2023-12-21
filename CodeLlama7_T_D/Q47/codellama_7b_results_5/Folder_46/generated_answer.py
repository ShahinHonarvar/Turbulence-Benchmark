 def palindromes_of_specific_lengths(string):
    # find the substring of interest
    substr = string[11:97]
    # initialize an empty set to store the palindromes
    palindromes = set()
    # loop through each character in the substring
    for i in range(len(substr)):
        # get the current character and its reverse
        char = substr[i]
        rev_char = substr[i].lower()[::-1]
        # check if the current character is a letter
        if char.isalpha():
            # check if the reverse of the current character is a letter
            if rev_char.isalpha():
                # loop through each length between 29 and 62 (both inclusive)
                for length in range(29, 63):
                    # get the substring of the specified length starting from the current index
                    sub_str = substr[i:i+length]
                    # check if the substring is a palindrome
                    if sub_str == sub_str[::-1]:
                        # add the palindrome to the set of palindromes
                        palindromes.add(sub_str)
    # return the set of palindromes in a case-insensitive manner
    return {p.lower() for p in palindromes}
