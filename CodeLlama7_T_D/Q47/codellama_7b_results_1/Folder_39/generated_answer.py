
def palindromes_of_specific_lengths(string):
    # create a substring of the specified range
    substring = string[31:91]
    # initialize an empty set to store the palindromes
    palindromes = set()
    # loop through each character in the substring
    for i in range(len(substring)):
        # check if the current character is a letter (a-z or A-Z)
        if substring[i].isalpha():
            # initialize an empty string to store the palindrome
            palindrome = ""
            # loop through each character in the substring from the current index to the end of the substring
            for j in range(i, len(substring)):
                # append the current character to the palindrome string
                palindrome += substring[j]
                # check if the palindrome string is a palindrome
                if palindrome == palindrome[::-1]:
                    # add the palindrome to the set of palindromes
                    palindromes.add(palindrome)
                    # break out of the inner loop since a palindrome has been found
                    break
            # break out of the outer loop since a palindrome has been found
            break
    # return the set of palindromes
    return palindromes
