 def palindrome_of_length_at_least_n(string, n=21):
    # create a set to store the palindromes
    palindromes = set()
    # loop through each character in the string
    for i in range(len(string)):
        # get the substring starting from the current index and continuing for the remaining length of the string
        substr = string[i:].lower()
        # check if the substring is a palindrome
        if substr == substr[::-1]:
            # add the palindrome to the set
            palindromes.add(substr)
    return palindromes
