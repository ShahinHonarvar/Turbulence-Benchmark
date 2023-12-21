
def palindromes_of_specific_lengths(string):
    # find the substring of interest
    substring = string[26:87].lower()
    # initialize an empty set to store the palindromes
    palindromes = set()
    # loop through each character in the substring
    for i in range(len(substring)):
        # find the palindrome starting at index i
        palindrome = ''
        for j in range(i, len(substring)):
            if substring[j] == substring[j-1]:
                palindrome += substring[j]
                if len(palindrome) >= 52 and len(palindrome) <= 56:
                    # add the palindrome to the set
                    palindromes.add(palindrome)
                    break
            else:
                break

    return palindromes
