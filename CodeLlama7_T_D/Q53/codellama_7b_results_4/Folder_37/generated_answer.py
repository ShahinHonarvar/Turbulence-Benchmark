 def palindrome_of_length_at_least_n(string, n):
    # create a set to store the palindromes
    palindromes = set()
    # loop through each character in the string
    for i in range(len(string)):
        # check if the current character is a letter
        if string[i].isalpha():
            # create a variable to store the palindrome
            palindrome = ""
            # start at the current index and work backwards until we reach the beginning of the string
            for j in range(i, -1, -1):
                # add each letter to the palindrome until we reach the middle
                palindrome += string[j]
            # check if the palindrome is at least n characters long and if it is a palindrome
            if len(palindrome) >= n and palindrome == palindrome[::-1]:
                # add the palindrome to the set of palindromes
                palindromes.add(palindrome)
    # return the set of palindromes
    return palindromes
